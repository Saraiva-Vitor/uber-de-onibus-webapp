# Generated by Django 4.2.5 on 2023-12-05 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uberdeonibusapp', '0032_alter_poltrona_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='poltrona',
            name='horario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uberdeonibusapp.busschedule'),
        ),
    ]
