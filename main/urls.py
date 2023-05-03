from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_trip/", views.create_trip, name="create_trip"),
    path("create_day/", views.create_day, name="create_day"),
    path("create_event/", views.create_event, name="create_event"),
    path("edit/<int:trip_id>/", views.edit_trip, name="edit_trip"),
    path("edit/<int:event_id>/", views.edit_event, name="edit_event"),
    path("delete/<int:trip_id>", views.delete_trip, name="delete_trip"),
]
