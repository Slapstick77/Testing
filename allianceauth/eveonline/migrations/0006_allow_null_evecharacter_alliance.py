# Generated by Django 1.10.1 on 2017-01-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveonline', '0005_remove_eveallianceinfo_member_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evecharacter',
            name='alliance_id',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='evecharacter',
            name='alliance_name',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
    ]
