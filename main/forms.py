from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput

from .models import Day, Event, Trip


class UserForm(UserCreationForm):
    username = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control my-3"})
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
        widgets = {
            # "username": forms.TextInput(attrs={"class": "form-control"}), # doesn't work
            "first_name": forms.TextInput(attrs={"class": "form-control my-3"}),
            "last_name": forms.TextInput(attrs={"class": "form-control my-3"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = PasswordInput(
            attrs={"class": "form-control my-3"}
        )
        self.fields["password2"].widget = PasswordInput(
            attrs={"class": "form-control my-3"}
        )


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control my-3"}),
            "last_name": forms.TextInput(attrs={"class": "form-control my-3"}),
        }


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        # fields = "__all__"
        fields = ["name", "start_date", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "start_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
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
            "day": forms.HiddenInput(),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(
                choices=Event.CATEGORY_LIST, attrs={"class": "form-control"}
            ),
            "time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "cost": forms.NumberInput(
                attrs={"Step": 0.01, "min": 0, "class": "form-control"}
            ),
            "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
        }
