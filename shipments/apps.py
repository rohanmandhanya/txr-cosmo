from django.apps import AppConfig

class ShipmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shipments'

    def ready(self):
        from .tasks import start_scheduler
        start_scheduler()
