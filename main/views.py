from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.template import loader
from .forms import DayForm, EventForm, TripForm
from .models import Event, Trip, Day


# Create your views here.
def index(request):
    trip = Trip.objects.get(pk=1)
    return render(request, "main/trips.html", {"trip": trip})


def create_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = TripForm()

    return render(request, "main/create_trip.html", {"form": form})


def edit_trip(request, trip_id):
    trip = Trip.objects.get(pk=trip_id)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = TripForm(instance=trip)

    return render(request, "main/edit_trip.html", {"form": form})


def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    trip.delete()
    return HttpResponseRedirect(reverse("index"))


def create_day(request):
    if request.method == "POST":
        form = DayForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = DayForm()

    return render(request, "main/create_day.html", {"form": form})


def edit_day(request, day_id):
    day = Day.objects.get(pk=day_id)
    if request.method == "POST":
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = DayForm(instance=day)

    return render(request, "main/edit_day.html", {"form": form})

def delete_day(request, day_id):
    day = get_object_or_404(Day, pk=day_id)
    day.delete()
    return HttpResponseRedirect(reverse("index"))

def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = EventForm()

    return render(request, "main/create_event.html", {"form": form})


def edit_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = EventForm(instance=event)

    return render(request, "main/edit_event.html", {"form": form})


def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return HttpResponseRedirect(reverse("index"))