# Generated by Django 4.2.5 on 2023-11-25 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uberdeonibusapp', '0025_remove_busschedule_poltronas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busschedule',
            name='schedule',
        ),
        migrations.AddField(
            model_name='busschedule',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='busschedule',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
