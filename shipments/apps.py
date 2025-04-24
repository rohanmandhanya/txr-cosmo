from django.apps import AppConfig

class ShipmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shipments'

    def ready(self):
        from django_celery_beat.models import PeriodicTask, IntervalSchedule
        from django.db.utils import OperationalError, ProgrammingError
        from celery import current_app

        try:
            schedule, _ = IntervalSchedule.objects.get_or_create(
                every=30,
                period=IntervalSchedule.MINUTES
            )

            if not PeriodicTask.objects.filter(name='Fetch CosmoCargo Shipments').exists():
                PeriodicTask.objects.create(
                    interval=schedule,
                    name='Fetch CosmoCargo Shipments',
                    task='shipments.tasks.fetch_and_store_shipments'
                )
        except (OperationalError, ProgrammingError):
            # Happens during first migrations or before tables are created
            pass
