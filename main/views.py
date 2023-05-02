from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Trip
from .forms import TripForm


# Create your views here.
def index(request):
    t = Trip.objects.get(pk=1)
    return render(request, "main/trips.html", {"trip": t})

def create_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))        
    else:
        form = TripForm()

    return render(request, "main/create_trip.html", {"form": form})