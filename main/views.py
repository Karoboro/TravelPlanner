from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .forms import DayForm, EventForm, TripForm
from .models import Day, Event, Trip


# Create your views here.
def index(request):
    trips = Trip.objects.all()  # Fetch all the trips
    context = {"trips": trips}
    return render(request, "main/trips.html", context)


def view_trip(request, trip_id):
    trips = Trip.objects.all()
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, "main/trips.html", {"trip": trip, "trips": trips})


def view_day(request, day_id):
    day = get_object_or_404(Day, pk=day_id)
    return render(request, "main/days.html", {"day": day})


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


def create_day(request, trip_id):
    if request.method == "POST":
        data = request.POST.dict()
        data.update({"trip": Trip.objects.get(pk=trip_id)})
        day_form = DayForm(data)
        event_form = EventForm(data)
        print(day_form.is_valid())
        print(event_form.is_valid())
        if day_form.is_valid() and event_form.is_valid():
            day_form.save()
            event_form.save()
            return HttpResponseRedirect(
                reverse("view_trip", kwargs={"trip_id": trip_id})
            )
    return render(request, "main/create_day.html")


def edit_day(request, day_id):
    day = Day.objects.get(pk=day_id)
    event_list = day.event_set.all()
    if request.method == "POST":
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = DayForm(instance=day)
        event_list = [EventForm(instance=event) for event in event_list]

    return render(
        request, "main/edit_day.html", {"form": form, "event_list": event_list}
    )


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
