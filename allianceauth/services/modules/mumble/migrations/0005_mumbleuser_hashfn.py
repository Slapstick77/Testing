# Generated by Django 1.10.4 on 2017-01-23 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mumble', '0004_auto_20161214_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='mumbleuser',
            name='hashfn',
            field=models.CharField(default='sha1', max_length=20),
        ),
        migrations.AlterField(
            model_name='mumbleuser',
            name='pwhash',
            field=models.CharField(max_length=80),
        ),
    ]
