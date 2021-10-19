# Generated by Django 1.10.5 on 2017-03-22 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srp', '0002_srpuserrequest_srp_status_choices'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='srpfleetmain',
            options={'permissions': (('access_srp', 'Can access SRP module'),)},
        ),
        migrations.AlterField(
            model_name='srpfleetmain',
            name='fleet_doctrine',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='srpfleetmain',
            name='fleet_name',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='srpfleetmain',
            name='fleet_srp_aar_link',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='srpfleetmain',
            name='fleet_srp_code',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='srpfleetmain',
            name='fleet_srp_status',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='srpuserrequest',
            name='additional_info',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='srpuserrequest',
            name='after_action_report_link',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='srpuserrequest',
            name='killboard_link',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='srpuserrequest',
            name='srp_ship_name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
