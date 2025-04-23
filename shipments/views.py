from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from datetime import datetime
import logging

from shipments.forms import ShipmentForm
from shipments.models import Shipment, Location, WeatherForecast
from shipments.serializers import ShipmentSerializer

logger = logging.getLogger(__name__)


class ShipmentListView(generics.ListAPIView):
    queryset = Shipment.objects.all().select_related('origin', 'destination', 'weather')
    serializer_class = ShipmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'origin__planet', 'destination__planet']
    search_fields = ['origin__address', 'destination__address']
    ordering_fields = ['shipment_time', 'eta_min', 'weight_kg']

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error fetching shipment list: {e}")
            return Response({"detail": "Error fetching shipments"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def shipment_dashboard(request):
    try:
        search = request.GET.get("search", "")
        shipments = Shipment.objects.select_related('origin', 'destination').all()

        if search:
            shipments = shipments.filter(
                Q(origin__address__icontains=search) |
                Q(destination__address__icontains=search)
            )

        return render(request, "shipments/dashboard.html", {"shipments": shipments})
    except Exception as e:
        logger.error(f"Error rendering dashboard: {e}")
        return render(request, "shipments/dashboard.html", {
            "shipments": [],
            "error": "Something went wrong while loading the dashboard."
        })


def create_shipment(request):
    try:
        if request.method == "POST":
            shipment_form = ShipmentForm(request.POST)

            if shipment_form.is_valid():
                origin, _ = Location.objects.get_or_create(
                    address=shipment_form.cleaned_data['origin_address'],
                    country=shipment_form.cleaned_data['origin_country'],
                    planet=shipment_form.cleaned_data['origin_planet'],
                    solar_system=shipment_form.cleaned_data['origin_solar_system'],
                )
                destination, _ = Location.objects.get_or_create(
                    address=shipment_form.cleaned_data['destination_address'],
                    country=shipment_form.cleaned_data['destination_country'],
                    planet=shipment_form.cleaned_data['destination_planet'],
                    solar_system=shipment_form.cleaned_data['destination_solar_system'],
                )
                weather, _ = WeatherForecast.objects.get_or_create(
                    wind_velocity_mph=shipment_form.cleaned_data['wind_velocity_mph'],
                    wind_direction=shipment_form.cleaned_data['wind_direction'],
                    precipitation_chance=shipment_form.cleaned_data['precipitation_chance'],
                    precipitation_kind=shipment_form.cleaned_data['precipitation_kind'],
                )

                Shipment.objects.create(
                    shipment_time=datetime.now(),
                    weight_kg=shipment_form.cleaned_data['weight_kg'],
                    volume_m3=shipment_form.cleaned_data['volume_m3'],
                    eta_min=shipment_form.cleaned_data['eta_min'],
                    status=shipment_form.cleaned_data['status'],
                    origin=origin,
                    destination=destination,
                    weather=weather
                )

                return redirect('shipment-dashboard')
        else:
            shipment_form = ShipmentForm()

        return render(request, "shipments/create_shipment.html", {
            "shipment_form": shipment_form
        })
    except Exception as e:
        logger.error(f"Error creating shipment: {e}")
        return render(request, "shipments/create_shipment.html", {
            "shipment_form": ShipmentForm(),
            "error": "An error occurred while creating the shipment."
        })
