from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view/trip/<int:trip_id>", views.view_trip, name="view_trip"),
    path("view/day/<int:day_id>", views.view_day, name="view_day"),
    path("create/trip", views.create_trip, name="create_trip"),
    path("edit/trip/<int:trip_id>", views.edit_trip, name="edit_trip"),
    path("delete/trip/<int:trip_id>", views.delete_trip, name="delete_trip"),
    path("add/day/<int:trip_id>", views.add_day, name="add_day"),
    path("edit/day/<int:day_id>", views.edit_day, name="edit_day"),
    path("delete/day/<int:day_id>", views.delete_day, name="delete_day"),
    path("create/event/<int:day_id>", views.create_event, name="create_event"),
    path("edit/event/<int:event_id>", views.edit_event, name="edit_event"),
    path("delete/event/<int:event_id>", views.delete_event, name="delete_event"),
    path("budget/", views.view_budget_page, name="view_budget_page"),
    path("budget/day/<int:trip_id>", views.budget_day, name="budget_day"),
    path(
        "budget/category/<int:trip_id>", views.budget_category, name="budget_category"
    ),
    path("accounts/create_user/", views.create_user, name="create_user"),
    path("accounts/profile", views.view_profile, name="profile"),
    path("accounts/edit/profile", views.edit_profile, name="edit_profile"),
    path("accounts/login/", views.LoginView.as_view(), name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
]
