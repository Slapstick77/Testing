# Generated by Django 3.2.9 on 2021-11-25 18:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groupmanagement', '0017_improve_groups_documentation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservedGroupName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name that can not be used for groups.', max_length=150, unique=True, verbose_name='name')),
                ('reason', models.TextField(help_text='Reason why this name is reserved.', verbose_name='reason')),
                ('created_by', models.CharField(help_text='Name of the user who created this entry.', max_length=255, verbose_name='created by')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Date when this entry was created', verbose_name='created at')),
            ],
        ),
    ]
