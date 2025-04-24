import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cosmo_cargo.settings')

app = Celery('cosmo_cargo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
