# Generated by Django 4.2.5 on 2023-11-03 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uberdeonibusapp', '0015_state_location_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uberdeonibusapp.state'),
        ),
    ]
