from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_trip/", views.create_trip, name="create_trip"),
    path("create_day/", views.create_day, name="create_day"),
    path("edit_day/<int:day_id>/", views.edit_day, name="edit_day"),
    path("create_event/", views.create_event, name="create_event"),
    path("edit/<int:trip_id>/", views.edit_trip, name="edit_trip"),
    path("edit/event/<int:event_id>/", views.edit_event, name="edit_event"),
    path("delete/trip/<int:trip_id>", views.delete_trip, name="delete_trip"),
    path("delete/event/<int:event_id>", views.delete_event, name="delete_event"),
]
