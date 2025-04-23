from django.db import models

class Location(models.Model):
    solar_system = models.CharField(max_length=100)
    planet = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    class Meta:
        unique_together = ('solar_system', 'planet', 'country', 'address')

    def __str__(self):
        return f"{self.address}, {self.planet} ({self.solar_system})"

class WeatherForecast(models.Model):
    wind_velocity_mph = models.FloatField()
    wind_direction = models.CharField(max_length=5)
    precipitation_chance = models.FloatField()
    precipitation_kind = models.CharField(max_length=50)

class Shipment(models.Model):
    shipment_time = models.DateTimeField()
    weight_kg = models.FloatField()
    volume_m3 = models.FloatField()
    eta_min = models.IntegerField()
    status = models.CharField(max_length=50)
    origin = models.ForeignKey(Location, related_name='origin_shipments', on_delete=models.CASCADE)
    destination = models.ForeignKey(Location, related_name='destination_shipments', on_delete=models.CASCADE)
    weather = models.ForeignKey(WeatherForecast, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Shipment #{self.id} - {self.status}"
