# Generated by Django 1.11.6 on 2017-10-09 09:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mumble', '0006_service_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mumbleuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='mumbleuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='mumble', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
