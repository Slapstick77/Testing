# Generated by Django 1.10.1 on 2016-09-06 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groupmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupdescription',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='hiddengroup',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
        ),
    ]
