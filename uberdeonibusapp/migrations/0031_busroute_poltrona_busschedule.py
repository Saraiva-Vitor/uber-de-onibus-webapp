# Generated by Django 4.2.5 on 2023-11-25 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uberdeonibusapp', '0030_remove_busschedule_route_remove_poltrona_passageiro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('bus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='uberdeonibusapp.bus')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_routes', to='uberdeonibusapp.location')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_routes', to='uberdeonibusapp.location')),
            ],
            options={
                'verbose_name': 'Rota',
                'verbose_name_plural': 'Rotas',
            },
        ),
        migrations.CreateModel(
            name='Poltrona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('ocupada', models.BooleanField(blank=True, default=False, null=True, verbose_name='Ocupada')),
                ('passageiro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uberdeonibusapp.customuser')),
                ('route', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uberdeonibusapp.busroute')),
            ],
            options={
                'verbose_name': 'Poltrona',
            },
        ),
        migrations.CreateModel(
            name='BusSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('hora', models.TimeField(blank=True, null=True)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uberdeonibusapp.busroute')),
            ],
            options={
                'verbose_name': 'Horário',
                'verbose_name_plural': 'Horários',
            },
        ),
    ]