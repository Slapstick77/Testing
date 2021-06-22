# Generated by Django 1.10.1 on 2016-09-05 21:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eveonline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='optimer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctrine', models.CharField(default=b'', max_length=254)),
                ('system', models.CharField(default=b'', max_length=254)),
                ('location', models.CharField(default=b'', max_length=254)),
                ('start', models.DateTimeField(default=datetime.datetime.now)),
                ('duration', models.CharField(default=b'', max_length=25)),
                ('operation_name', models.CharField(default=b'', max_length=254)),
                ('fc', models.CharField(default=b'', max_length=254)),
                ('details', models.CharField(default=b'', max_length=254)),
                ('post_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('eve_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eveonline.EveCharacter')),
            ],
            options={
                'ordering': ['start'],
            },
        ),
    ]
