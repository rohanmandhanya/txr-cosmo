from django import forms

class ShipmentForm(forms.Form):

    weight_kg = forms.FloatField()
    volume_m3 = forms.FloatField()
    eta_min = forms.IntegerField()
    status = forms.ChoiceField(choices=[('shipped', 'Shipped'), ('in_transit', 'In Transit'), ('delivered', 'Delivered')])

    # Origin fields
    origin_address = forms.CharField()
    origin_country = forms.CharField()
    origin_planet = forms.CharField()
    origin_solar_system = forms.CharField()

    # Destination fields
    destination_address = forms.CharField()
    destination_country = forms.CharField()
    destination_planet = forms.CharField()
    destination_solar_system = forms.CharField()

    # Weather fields
    wind_velocity_mph = forms.FloatField()
    wind_direction = forms.CharField()
    precipitation_chance = forms.FloatField()
    precipitation_kind = forms.CharField()
