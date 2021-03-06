# Generated by Django 1.10.1 on 2016-09-05 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eveonline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(default=b'', max_length=254)),
                ('system', models.CharField(default=b'', max_length=254)),
                ('planet_moon', models.CharField(default=b'', max_length=254)),
                ('structure', models.CharField(default=b'', max_length=254)),
                ('objective', models.CharField(default=b'', max_length=254)),
                ('eve_time', models.DateTimeField()),
                ('important', models.BooleanField(default=False)),
                ('corp_timer', models.BooleanField(default=False)),
                ('eve_character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eveonline.EveCharacter')),
                ('eve_corp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eveonline.EveCorporationInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['eve_time'],
            },
        ),
    ]
