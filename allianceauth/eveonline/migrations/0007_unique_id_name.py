# Generated by Django 1.10.5 on 2017-01-18 13:20

from django.db import migrations, models


def get_duplicates(items):
    return {item for item in items if items.count(item) > 1}


def enforce_unique_characters(apps, schema_editor):
    EveCharacter = apps.get_model('eveonline', 'EveCharacter')

    ids = [c.character_id for c in EveCharacter.objects.all()]
    duplicates = get_duplicates(ids)
    for c_id in duplicates:
        dupes = EveCharacter.objects.filter(character_id=c_id)
        dupes.exclude(pk=dupes[0].pk).delete()

    names = [c.character_name for c in EveCharacter.objects.all()]
    duplicates = get_duplicates(names)
    for name in duplicates:
        dupes = EveCharacter.objects.filter(character_name=name)
        dupes.exclude(pk=dupes[0].pk).delete()


def enforce_unique_corporations(apps, schema_editor):
    EveCorporationInfo = apps.get_model('eveonline', 'EveCorporationInfo')

    ids = [c.corporation_id for c in EveCorporationInfo.objects.all()]
    duplicates = get_duplicates(ids)
    for c_id in duplicates:
        dupes = EveCorporationInfo.objects.filter(corporation_id=c_id)
        dupes.exclude(pk=dupes[0].pk).delete()

    names = [c.corporation_name for c in EveCorporationInfo.objects.all()]
    duplicates = get_duplicates(names)
    for name in duplicates:
        dupes = EveCorporationInfo.objects.filter(character_name=name)
        dupes.exclude(pk=dupes[0].pk).delete()


def enforce_unique_alliances(apps, schema_editor):
    EveAllianceInfo = apps.get_model('eveonline', 'EveAllianceInfo')
    EveCorporationInfo = apps.get_model('eveonline', 'EveCorporationInfo')

    ids = [a.alliance_id for a in EveAllianceInfo.objects.all()]
    duplicates = get_duplicates(ids)
    for a_id in duplicates:
        dupes = EveAllianceInfo.objects.filter(alliance_id=a_id)
        to_be_kept = dupes[0]
        EveCorporationInfo.objects.filter(alliance__pk__in=[a.pk for a in dupes.exclude(pk=to_be_kept.pk)]).update(
            alliance=to_be_kept.pk)
        dupes.exclude(pk=to_be_kept.pk).delete()

    names = [a.alliance_name for a in EveAllianceInfo.objects.all()]
    duplicates = get_duplicates(names)
    for name in duplicates:
        dupes = EveAllianceInfo.objects.filter(alliance_name=name)
        to_be_kept = dupes[0]
        EveCorporationInfo.objects.filter(alliance__in=[a.pk for a in dupes.exclude(pk=to_be_kept.pk)]).update(
            alliance=to_be_kept.pk)
        dupes.exclude(pk=to_be_kept.pk).delete()


def enforce_unique_apis(apps, schema_editor):
    EveApiKeyPair = apps.get_model('eveonline', 'EveApiKeyPair')

    ids = [api.api_id for api in EveApiKeyPair.objects.all()]
    duplicates = get_duplicates(ids)
    for api_id in duplicates:
        dupes = EveApiKeyPair.objects.filter(api_id=api_id)
        dupes.exclude(pk=dupes[0].pk).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('eveonline', '0006_allow_null_evecharacter_alliance'),
    ]

    operations = [
        migrations.RunPython(enforce_unique_characters, migrations.RunPython.noop),
        migrations.RunPython(enforce_unique_corporations, migrations.RunPython.noop),
        migrations.RunPython(enforce_unique_alliances, migrations.RunPython.noop),
        migrations.RunPython(enforce_unique_apis, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='evecharacter',
            name='character_id',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='evecharacter',
            name='character_name',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='evecorporationinfo',
            name='corporation_id',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='evecorporationinfo',
            name='corporation_name',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='eveallianceinfo',
            name='alliance_id',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='eveallianceinfo',
            name='alliance_name',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='eveapikeypair',
            name='api_id',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
