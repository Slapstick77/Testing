# Every setting in base.py can be overloaded by redefining it here.
from .base import *

SECRET_KEY = os.environ.get("AA_SECRET_KEY")
SITE_NAME = os.environ.get("AA_SITENAME")
DEBUG = os.environ.get("AA_DEBUG", False)
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': os.environ.get("AA_DB_NAME"),
    'USER': os.environ.get("AA_DB_USER"),
    'PASSWORD': os.environ.get("AA_DB_PASSWORD"),
    'HOST': os.environ.get("AA_DB_HOST"),
    'PORT': os.environ.get("AA_DB_PORT", "3306"),
}

# Register an application at https://developers.eveonline.com for Authentication
# & API Access and fill out these settings. Be sure to set the callback URL
# to https://example.com/sso/callback substituting your domain for example.com
# Logging in to auth requires the publicData scope (can be overridden through the
# LOGIN_TOKEN_SCOPES setting). Other apps may require more (see their docs).

ESI_SSO_CLIENT_ID = os.environ.get("ESI_SSO_CLIENT_ID")
ESI_SSO_CLIENT_SECRET = os.environ.get("ESI_SSO_CLIENT_SECRET")
ESI_SSO_CALLBACK_URL = (f"{os.environ.get('PROTOCOL')}"
                        f"{os.environ.get('AUTH_SUBDOMAIN')}."
                        f"{os.environ.get('DOMAIN')}/sso/callback")
ESI_USER_CONTACT_EMAIL = os.environ.get("ESI_USER_CONTACT_EMAIL")    # A server maintainer that CCP can contact in case of issues.

# By default emails are validated before new users can log in.
# It's recommended to use a free service like SparkPost or Elastic Email to send email.
# https://www.sparkpost.com/docs/integrations/django/
# https://elasticemail.com/resources/settings/smtp-api/
# Set the default from email to something like 'noreply@example.com'
# Email validation can be turned off by uncommenting the line below. This can break some services.
REGISTRATION_VERIFY_EMAIL = False
EMAIL_HOST = os.environ.get("AA_EMAIL_HOST", "")
EMAIL_PORT = os.environ.get("AA_EMAIL_PORT", 587)
EMAIL_HOST_USER = os.environ.get("AA_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("AA_EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = os.environ.get("AA_EMAIL_USE_TLS", True)
DEFAULT_FROM_EMAIL = os.environ.get("AA_DEFAULT_FROM_EMAIL", "")

ROOT_URLCONF = 'myauth.urls'
WSGI_APPLICATION = 'myauth.wsgi.application'
STATIC_ROOT = "/var/www/myauth/static/"
BROKER_URL = F"redis://{os.environ.get('AA_REDIS', 'redis:6379')}/0"
CELERY_RESULT_BACKEND = F"redis://{os.environ.get('AA_REDIS', 'redis:6379')}/0"
CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": os.environ.get('AA_REDIS', 'redis:6379'),
        "OPTIONS": {
            "DB": 1,
        }
    }
}

# Add any additional apps to this list.
INSTALLED_APPS += [
# https://allianceauth.readthedocs.io/en/latest/features/apps/index.html
# 'allianceauth.corputils',
# 'allianceauth.fleetactivitytracking',
# 'allianceauth.optimer',
# 'allianceauth.permissions_tool',
# 'allianceauth.srp',
# 'allianceauth.timerboard',

# https://allianceauth.readthedocs.io/en/latest/features/services/index.html
# 'allianceauth.services.modules.discord',
# 'allianceauth.services.modules.discourse',
# 'allianceauth.services.modules.ips4',
# 'allianceauth.services.modules.openfire',
# 'allianceauth.services.modules.phpbb3',
# 'allianceauth.services.modules.smf',
# 'allianceauth.services.modules.teamspeak3',
# 'allianceauth.services.modules.xenforo',
]

#######################################
# Add any custom settings below here. #
#######################################