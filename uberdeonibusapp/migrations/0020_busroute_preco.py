# Generated by Django 4.2.5 on 2023-11-24 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uberdeonibusapp', '0019_customuser_delete_profiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='busroute',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
