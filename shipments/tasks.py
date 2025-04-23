import requests
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler


from shipments.models import Shipment, Location, WeatherForecast
from shipments.utils import fetch_shipments_with_js


def fetch_and_store_shipments():
    shipments = fetch_shipments_with_js()

    for data in shipments:
        origin, _ = Location.objects.get_or_create(
            solar_system=data["originSolarSystem"],
            planet=data["originPlanet"],
            country=data["originCountry"],
            address=data["originAddress"]
        )
        destination, _ = Location.objects.get_or_create(
            solar_system=data["destinationSolarSystem"],
            planet=data["destinationPlanet"],
            country=data["destinationCountry"],
            address=data["destinationAddress"]
        )
        weather = WeatherForecast.objects.create(
            wind_velocity_mph=data["forecastOriginWindVelocityMph"],
            wind_direction=data["forecastOriginWindDirection"],
            precipitation_chance=data["forecastOriginPrecipitationChance"],
            precipitation_kind=data["forecastOriginPrecipitationKind"]
        )

        Shipment.objects.create(
            shipment_time=datetime.fromtimestamp(data["time"]),
            weight_kg=data["weightKg"],
            volume_m3=data["volumeM3"],
            eta_min=data["etaMin"],
            status=data["status"],
            origin=origin,
            destination=destination,
            weather=weather
        )



def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_store_shipments, 'interval', minutes=30)
    scheduler.start()
