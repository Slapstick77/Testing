# Generated by Django 1.10.2 on 2016-12-12 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mumble', '0002_auto_20161212_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='mumbleuser',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mumble', to=settings.AUTH_USER_MODEL),
        ),
    ]
