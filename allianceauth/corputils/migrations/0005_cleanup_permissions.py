# Generated by Django 1.11.2 on 2017-06-10 15:34

from django.db import migrations


def delete_permissions(apps, schema_editor):
    CorpStats = apps.get_model('corputils', 'CorpStats')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Permission = apps.get_model('auth', 'Permission')
    ct = ContentType.objects.get_for_model(CorpStats)
    perms = Permission.objects.filter(content_type=ct)
    perms.filter(codename__contains='api').delete()
    perms.filter(codename='view_corpstats').delete()
    perms.filter(codename__contains='blue').delete()
    perms.filter(codename__contains='remove').delete()

    g = perms.get(codename='view_corp_corpstats')
    g.name = 'Can view corp stats of their corporation.'
    g.save()

    g = perms.get(codename='view_alliance_corpstats')
    g.name = 'Can view corp stats of members of their alliance.'
    g.save()


class Migration(migrations.Migration):

    dependencies = [
        ('corputils', '0004_member_models'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='corpstats',
            options={'permissions': (('view_corp_corpstats', 'Can view corp stats of their corporation.'), ('view_alliance_corpstats', 'Can view corp stats of members of their alliance.'), ('view_state_corpstats', 'Can view corp stats of members of their auth state.')), 'verbose_name': 'corp stats', 'verbose_name_plural': 'corp stats'},
        ),
        migrations.RunPython(delete_permissions, migrations.RunPython.noop),
    ]
