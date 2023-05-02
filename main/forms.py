from django import forms
from .models import Trip, Day, Event

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ["name", "description"]