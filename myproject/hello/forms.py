# hello/forms.py

from django import forms

class HousePriceForm(forms.Form):
    beds = forms.IntegerField(label='Beds', min_value=1)
    baths = forms.FloatField(label='Baths', min_value=1.0)
    size = forms.IntegerField(label='Size (sqft)', min_value=100)
