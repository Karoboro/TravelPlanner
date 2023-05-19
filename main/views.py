from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import DayForm, EventForm, TripForm, UserForm
from .models import Day, Event, Trip


class LoginView(LoginView):
    next_page = "/"
    redirect_authenticated_user = True


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.username
            user.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserForm()

    return render(request, "registration/create_user.html", {"form": form})


@login_required
def view_profile(request):
    if request.method == "POST":
        print(request.POST)
    context = {"user": request.user}
    return render(request, "registration/profile.html", context)


# Create your views here.
def index(request):
    user = request.user
    trips = (
        user.trip_set.all() if user.is_authenticated else None
    )  # Fetch all the trips
    context = {"trips": trips, "user": request.user}
    return render(request, "main/trips.html", context)


@login_required
def view_trip(request, trip_id):
    user = request.user
    trips = user.trip_set.all()
    trip = get_object_or_404(trips, pk=trip_id)
    return render(request, "main/trips.html", {"trip": trip, "trips": trips})


@login_required
def view_day(request, day_id):
    user = request.user
    days = Day.objects.filter(trip__in=user.trip_set.all())
    day = get_object_or_404(days, pk=day_id)
    return render(request, "main/days.html", {"day": day})


# def create_trip(request):
#     if request.method == "POST":
#         form = TripForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("index"))
#     else:
#         form = TripForm()

#     return render(request, "main/create_trip.html", {"form": form})


@login_required
def create_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user
            trip.save()
            # Create the first Day for this Trip
            # see comment in add_day on how create and save interact
            Day.objects.create(trip=trip)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = TripForm()

    return render(request, "main/create_trip.html", {"form": form})


@login_required
def edit_trip(request, trip_id):
    user = request.user
    trip = get_object_or_404(user.trip_set.all(), pk=trip_id)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("view_trip", kwargs={"trip_id": trip_id})
            )
    else:
        form = TripForm(instance=trip)

    return render(request, "main/edit_trip.html", {"form": form})


@login_required
def delete_trip(request, trip_id):
    user = request.user
    trip = get_object_or_404(user.trip_set.all(), pk=trip_id)
    trip.delete()
    return HttpResponseRedirect(reverse("index"))


# def create_day(request, trip_id):
#     if request.method == "POST":
#         form = DayForm(request.POST, initial={"trip": Trip.objects.get(pk=trip_id)})
#         form.fields["trip"].widget = forms.HiddenInput()
#         form.fields["trip"].initial = Trip.objects.get(pk=trip_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(
#                 reverse("view_trip", kwargs={"trip_id": trip_id})
#             )

#     else:
#         form = DayForm(initial={"trip": Trip.objects.get(pk=trip_id)})
#         form.fields["trip"].widget = forms.HiddenInput()
#         form.fields["trip"].initial = Trip.objects.get(pk=trip_id)

#     return render(request, "main/create_day.html", {"form": form})


@login_required
def add_day(request, trip_id):
    user = request.user
    trip = get_object_or_404(user.trip_set.all(), pk=trip_id)

    if request.method == "GET":
        # create does 2 things: create an object & save it in the database
        # since we are overriding the save method, our custom save method is called
        day = Day.objects.create(trip=trip)
        return HttpResponseRedirect(reverse("view_trip", kwargs={"trip_id": trip_id}))

    return HttpResponseRedirect(reverse("index"))


@login_required
def edit_day(request, day_id):
    user = request.user
    days = Day.objects.filter(trip__in=user.trip_set.all())
    day = get_object_or_404(days, pk=day_id)
    event_list = day.event_set.all()
    if request.method == "POST":
        form = DayForm(request.POST, instance=day)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("view_trip", kwargs={"trip_id": day.trip.pk})
            )
    else:
        form = DayForm(instance=day)
        event_list = [EventForm(instance=event) for event in event_list]

    return render(
        request, "main/edit_day.html", {"form": form, "event_list": event_list}
    )


@login_required
def delete_day(request, day_id):
    user = request.user
    days = Day.objects.filter(trip__in=user.trip_set.all())
    day = get_object_or_404(days, pk=day_id)
    trip_id = day.trip.pk
    day.delete()
    return HttpResponseRedirect(reverse("view_trip", kwargs={"trip_id": trip_id}))


@login_required
def create_event(request, day_id):
    user = request.user
    days = Day.objects.filter(trip__in=user.trip_set.all())
    day = get_object_or_404(days, pk=day_id)
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.day = day
            event.save()
            return HttpResponseRedirect(reverse("view_day", args=[day_id]))
    else:
        form = EventForm(initial={"day": day})
        form.fields["day"].widget = forms.HiddenInput()

    return render(request, "main/create_event.html", {"form": form})


@login_required
def edit_event(request, event_id):
    user = request.user
    days = Day.objects.filter(trip__in=user.trip_set.all())
    events = Event.objects.filter(day__in=days)
    event = get_object_or_404(events, pk=event_id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        form.fields["day"].widget = forms.HiddenInput()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("view_day", kwargs={"day_id": event.day.pk})
            )
    else:
        form = EventForm(instance=event)
        form.fields["day"].widget = forms.HiddenInput()

    return render(request, "main/edit_event.html", {"form": form})


@login_required
def delete_event(request, event_id):
    user = request.user
    days = Day.objects.filter(trip__in=user.trip_set.all())
    events = Event.objects.filter(day__in=days)
    event = get_object_or_404(events, pk=event_id)
    day_id = event.day.pk
    event.delete()
    return HttpResponseRedirect(reverse("view_day", kwargs={"day_id": day_id}))


@login_required
def view_budget_page(request):
    user = request.user
    trips = user.trip_set.all()
    return render(request, "main/budget_day.html", {"trips": trips})


@login_required
def budget_day(request, trip_id):
    user = request.user
    trips = user.trip_set.all()
    # access with budget/day/1
    trip = get_object_or_404(trips, pk=trip_id)
    days = trip.day_set.all()
    total = 0
    day_expense = []

    for day in days:
        cost = sum([event.cost for event in day.event_set.all()])
        day_expense.append((day, cost))
        total += cost
    # print(day)
    # print(day_expense)
    return render(
        request,
        "main/budget_day.html",
        {"day_expense": day_expense, "total": total, "trips": trips, "trip": trip},
    )


@login_required
def budget_category(request, trip_id):
    user = request.user
    trips = user.trip_set.all()
    trip = get_object_or_404(trips, pk=trip_id)
    total = sum(trip.generate_expense_dict().values())
    return render(
        request,
        "main/budget_category.html",
        {"trip": trip, "total": total, "trips": trips},
    )
