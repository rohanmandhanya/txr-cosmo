from rest_framework import serializers
from shipments.models import Shipment, Location, WeatherForecast

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class WeatherForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    origin = LocationSerializer()
    destination = LocationSerializer()
    weather = WeatherForecastSerializer()

    class Meta:
        model = Shipment
        fields = '__all__'
