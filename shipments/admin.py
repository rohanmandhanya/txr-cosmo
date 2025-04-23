# shipments/admin.py

from django.contrib import admin
from shipments.models import Shipment, Location, WeatherForecast

admin.site.register(Shipment)
admin.site.register(Location)
admin.site.register(WeatherForecast)
