from django import forms

from .models import Day, Event, Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ["name", "description"]


class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ["trip", "num"]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["day", "name", "category", "time", "location", "cost", "description"]
