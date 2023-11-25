from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta, datetime
from .models import *

@receiver(post_save, sender=BusRoute)
def criar_horarios_poltronas(sender, instance, created, **kwargs):
    if created:
        for day_offset in range(1, 6):  # Criando horários para os próximos 5 dias
            for i in range(6, 22):  # Criando 5 horários como exemplo
                schedule_date = timezone.now() + timedelta(days=day_offset)
                schedule_time = datetime.combine(schedule_date, datetime.min.time()) + timedelta(hours=i)
                BusSchedule.objects.create(route=instance, date=schedule_date, time=schedule_time)

        # Vincule automaticamente as poltronas
        for numero_poltrona in range(1, 49):  # Vinculando 48 poltronas como exemplo
            Poltrona.objects.create(route=instance, numero=numero_poltrona)