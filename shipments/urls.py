from django.urls import path
from shipments.views import ShipmentListView, shipment_dashboard, create_shipment

urlpatterns = [
    path('shipments/', ShipmentListView.as_view(), name='shipment-list'),
    path('dashboard/new/', create_shipment, name='create-shipment'),
]
