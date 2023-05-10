from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/trip/<int:trip_id>", views.view_trip, name="view_trip"),
    path("view/day/<int:day_id>", views.view_day, name="view_day"),
    path("create/trip/", views.create_trip, name="create_trip"),
    path("edit/trip/<int:trip_id>/", views.edit_trip, name="edit_trip"),
    path("delete/trip/<int:trip_id>", views.delete_trip, name="delete_trip"),
    path("create/day/<int:trip_id>", views.create_day, name="create_day"),
    path("edit/day/<int:day_id>/", views.edit_day, name="edit_day"),
    path("delete/day/<int:day_id>", views.delete_day, name="delete_day"),
    path("create/event/<int:day_id>", views.create_event, name="create_event"),
    path("edit/event/<int:event_id>/", views.edit_event, name="edit_event"),
    path("delete/event/<int:event_id>", views.delete_event, name="delete_event"),
    path("budget/day/<int:trip_id>", views.budget_day, name="budget_day"),
    path("budget/category/<int:trip_id>", views.budget_category, name="budget_category"),
]
