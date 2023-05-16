from typing import Any, Dict, Mapping, Optional, Type, Union

from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import Day, Event, Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        # fields = "__all__"
        fields = ["name", "start_date", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }

class DayForm(forms.ModelForm):
    trip = forms.ModelChoiceField(queryset=Trip.objects.all(), empty_label=None)

    class Meta:
        model = Day
        fields = ["trip"]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["day", "name", "category", "time", "location", "cost", "description"]
        widgets = {
            "time": forms.TimeInput(attrs={"type": "time"}),
            "cost": forms.NumberInput(attrs={"Step": 0.01, "min": 0}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }
