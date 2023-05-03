from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_trip/", views.create_trip, name="create_trip"),
    path("create_day/", views.create_day, name="create_day"),
    path("create_activity/", views.create_activity, name="create_activity"),
    # path("edit/<int:trip_id>/<int:day>/<int:activity_id>/", views.edit_activity, name="edit_activity")
    path("edit/activity/<int:id>", views.edit_activity, name="edit_activity"),
]
