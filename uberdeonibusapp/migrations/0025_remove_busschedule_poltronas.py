# Generated by Django 4.2.5 on 2023-11-25 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uberdeonibusapp', '0024_poltrona_route_remove_busschedule_poltronas_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busschedule',
            name='poltronas',
        ),
    ]
