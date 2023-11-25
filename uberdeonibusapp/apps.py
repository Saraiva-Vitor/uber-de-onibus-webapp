from django.apps import AppConfig

class UberdeonibusappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uberdeonibusapp'

    def ready(self):
        import uberdeonibusapp.signals