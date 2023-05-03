from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_trip/", views.create_trip, name="create_trip"),
    path("create_day/", views.create_day, name="create_day"),
    path("create_event/", views.create_event, name="create_event"),
]
