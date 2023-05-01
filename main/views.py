from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Trip


# Create your views here.
def index(request):
    t = Trip.objects.get(pk=1)
    return render(request, "main/trips.html", {"trip": t})
