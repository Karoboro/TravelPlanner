from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Day, Event, Trip


class UserForm(UserCreationForm):
    username = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        # fields = "__all__"
        fields = ["name", "start_date", "description"]
        widgets = {"start_date": forms.DateInput(attrs={"type": "date"})}


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
