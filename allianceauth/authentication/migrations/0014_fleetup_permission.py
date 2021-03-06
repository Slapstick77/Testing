# Generated by Django 1.10.1 on 2016-09-09 23:19

from django.db import migrations


def create_permission(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')
    ct = ContentType.objects.get_for_model(User)
    Permission.objects.get_or_create(codename="view_fleetup", content_type=ct, name="view_fleetup")


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_service_modules'),
    ]

    operations = [
        migrations.RunPython(create_permission, migrations.RunPython.noop)
    ]
