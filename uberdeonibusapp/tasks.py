# tasks.py
from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import *

@shared_task
def atualizar_registro(registro_id):
    # Lógica para atualizar o registro
    registro = Poltrona.objects.get(pk=registro_id)
    registro.ocupada = False
    registro.save()
    print(registro.ocupada)
