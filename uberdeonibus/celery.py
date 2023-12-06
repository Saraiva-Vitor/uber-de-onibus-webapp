# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o nome do projeto Django para que o Celery possa encontrá-lo.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seuprojeto.settings')

# Cria uma instância do Celery usando o mesmo objeto de configuração do Django.
app = Celery('seuprojeto')

# Configurações do Celery, leia mais na documentação do Celery.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carrega tarefas do Django.
app.autodiscover_tasks()
