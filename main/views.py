from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.template import loader
from .forms import DayForm, EventForm, TripForm
from .models import Trip, Event


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


def create_day(request):
    if request.method == "POST":
        form = DayForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("index"))
    else:
        form = DayForm()

    return render(request, "main/create_day.html", {"form": form})


def create_activity(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = EventForm()

    return render(request, "main/create_activity.html", {"form": form})


def edit_activity(request, id):
    activity = Event.objects.get(id=id)
    template = loader.get_template('main/edit_activity.html')
    context = {
    'activity': activity,
    }
    return HttpResponse(template.render(context, request))