from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.urls import reverse

from allianceauth.tests.auth_utils import AuthUtils

from . import MODULE_PATH, add_permissions_to_members, TEST_USER_NAME, TEST_USER_ID
from ..models import DiscordUser, DiscordClient
from ..utils import set_logger_to_file
from ..views import (
    discord_callback, 
    reset_discord, 
    deactivate_discord, 
    discord_add_bot, 
    activate_discord
)


logger = set_logger_to_file(MODULE_PATH + '.views', __file__)


class SetupClassMixin(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.factory = RequestFactory()
        cls.user = AuthUtils.create_member(TEST_USER_NAME)
        add_permissions_to_members()
        cls.services_url = reverse('services:services')


class TestActivateDiscord(SetupClassMixin, TestCase):

    @patch(MODULE_PATH + '.views.DiscordUser.objects.generate_oauth_redirect_url')
    def test_redirects_to_correct_url(self, mock_generate_oauth_redirect_url):
        expected_url = '/example.com/oauth/'
        mock_generate_oauth_redirect_url.return_value = expected_url
        request = self.factory.get(reverse('discord:activate'))
        request.user = self.user
        response = activate_discord(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, expected_url)


@patch(MODULE_PATH + '.views.messages')
@patch(MODULE_PATH + '.managers.DiscordClient', spec=DiscordClient)
class TestDeactivateDiscord(SetupClassMixin, TestCase):
    
    def setUp(self):
        DiscordUser.objects.create(user=self.user, uid=TEST_USER_ID)
    
    def test_when_successful_show_success_message(
        self, mock_DiscordClient, mock_messages
    ):
        mock_DiscordClient.return_value.remove_guild_member.return_value = True
        request = self.factory.get(reverse('discord:deactivate'))
        request.user = self.user
        response = deactivate_discord(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.services_url)
        self.assertTrue(mock_messages.success.called)
        self.assertFalse(mock_messages.error.called)

    def test_when_unsuccessful_show_error_message(
        self, mock_DiscordClient, mock_messages
    ):
        mock_DiscordClient.return_value.remove_guild_member.return_value = False
        request = self.factory.get(reverse('discord:deactivate'))
        request.user = self.user
        response = deactivate_discord(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.services_url)
        self.assertFalse(mock_messages.success.called)
        self.assertTrue(mock_messages.error.called)


@patch(MODULE_PATH + '.views.messages')
@patch(MODULE_PATH + '.managers.DiscordClient')
class TestResetDiscord(SetupClassMixin, TestCase):
    
    def setUp(self):
        DiscordUser.objects.create(user=self.user, uid=TEST_USER_ID)

    def test_when_successful_redirect_to_activate(
        self, mock_DiscordClient, mock_messages
    ):
        mock_DiscordClient.return_value.remove_guild_member.return_value = True
        request = self.factory.get(reverse('discord:reset'))
        request.user = self.user
        response = reset_discord(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("discord:activate"))        
        self.assertFalse(mock_messages.error.called)

    def test_when_unsuccessful_message_error_and_redirect_to_service(
        self, mock_DiscordClient, mock_messages
    ):
        mock_DiscordClient.return_value.remove_guild_member.return_value = False
        request = self.factory.get(reverse('discord:reset'))
        request.user = self.user
        response = reset_discord(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.services_url)
        self.assertTrue(mock_messages.error.called)


@patch(MODULE_PATH + '.views.messages')
@patch(MODULE_PATH + '.views.DiscordUser.objects.add_user')
class TestDiscordCallback(SetupClassMixin, TestCase):
    
    def setUp(self):
        DiscordUser.objects.create(user=self.user, uid=TEST_USER_ID)

    def test_success_message_when_ok(self, mock_add_user, mock_messages):
        mock_add_user.return_value = True
        request = self.factory.get(
            reverse('discord:callback'), data={'code': '1234'}
        )
        request.user = self.user
        response = discord_callback(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.services_url)
        self.assertTrue(mock_messages.success.called)
        self.assertFalse(mock_messages.error.called)
    
    def test_handle_no_code(self, mock_add_user, mock_messages):
        mock_add_user.return_value = True
        request = self.factory.get(
            reverse('discord:callback'), data={}
        )
        request.user = self.user
        response = discord_callback(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.services_url)
        self.assertFalse(mock_messages.success.called)
        self.assertTrue(mock_messages.error.called)
    
    def test_error_message_when_user_creation_failed(
        self, mock_add_user, mock_messages
    ):
        mock_add_user.return_value = False
        request = self.factory.get(
            reverse('discord:callback'), data={'code': '1234'}
        )
        request.user = self.user
        response = discord_callback(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.services_url)
        self.assertFalse(mock_messages.success.called)
        self.assertTrue(mock_messages.error.called)


@patch(MODULE_PATH + '.views.DiscordUser.objects.generate_bot_add_url')
class TestDiscordAddBot(TestCase):
    
    def test_add_bot(self, mock_generate_bot_add_url):
        bot_url = 'https://www.example.com/bot'
        mock_generate_bot_add_url.return_value = bot_url
        my_user = User.objects.create_superuser('Lex Luthor', 'abc', 'def')
        request = RequestFactory().get(reverse('discord:add_bot'))
        request.user = my_user
        response = discord_add_bot(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, bot_url)
