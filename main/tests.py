from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import Client, TestCase
from django.test.utils import setup_test_environment

from .models import Event, Trip


# Create your tests here.
class TripModelTests(TestCase):
    def setUp(self):
        user = User.objects.create_user("admin", "", "admin")
        Trip.objects.create(
            name="Trip to Somewhere", description="A testing trip", user=user
        )

    def test_number_of_days(self):
        trip = Trip.objects.get(name="Trip to Somewhere")
        trip.day_set.create(num=1)
        trip.day_set.create(num=2)
        trip.day_set.create(num=3)
        self.assertIs(len(trip), 3)

    # def test_invalid_duplicate_day(self):
    #     with self.assertRaises(IntegrityError):
    #         trip = Trip.objects.get(name="Trip to Somewhere")
    #         trip.day_set.create(num=1)
    #         trip.day_set.create(num=1)

    # def test_invalid_neg_day_num(self):
    #     with self.assertRaises(IntegrityError):
    #         trip = Trip.objects.get(name="Trip to Somewhere")
    #         trip.day_set.create(num=-1)

    def test_invalid_event_cost(self):
        with self.assertRaises(IntegrityError):
            trip = Trip.objects.get(name="Trip to Somewhere")
            day = trip.day_set.create(num=1)
            day.save()
            event = day.event_set.create(
                name="Ramen",
                category="Food",
                time="13:00",
                location="Restaurant",
                cost="-10",
                description="Good ramen",
            )

    def test_delete_event(self):
        trip = Trip.objects.get(name="Trip to Somewhere")
        day = trip.day_set.create(num=1)
        day.save()
        event = day.event_set.create(
            name="Ramen",
            category="Food",
            time="13:00",
            location="Restaurant",
            cost="20",
            description="Good ramen",
        )
        self.assertIs(len(day), 1)
        event.delete()
        self.assertIs(len(day), 0)


class ModelBudgetTests(TestCase):
    fixtures = ["test_db.json"]

    def test_budget_total(self):
        trip = Trip.objects.get(pk=1)
        self.assertEqual(sum(trip.generate_day_expense().values()), 535)


class EndpointTests(TestCase):
    def setUp(self):
        user = User.objects.create_user("admin", "", "admin")
        user2 = User.objects.create_user("user2", "", "user2")
        Trip.objects.create(
            name="Trip to Somewhere", description="A testing trip", user=user
        )
        Trip.objects.create(
            name="User2 Trip", description="admin user should not see this", user=user2
        )

    def test_landing_page(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")
        self.assertContains(response, "Welcome to BonVoyage!")

    def test_trip_view(self):
        response = self.client.post(
            "/accounts/login/", {"username": "admin", "password": "admin"}
        )
        response = self.client.get("/view/trip/1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A testing trip")

    def test_user_based_view(self):
        response = self.client.post(
            "/accounts/login/", {"username": "admin", "password": "admin"}
        )
        response = self.client.get("/view/trip/2")
        self.assertEqual(response.status_code, 404)


class FixtureEndpointTests(TestCase):
    fixtures = ["test_db.json"]

    def test_create_day(self):
        response = self.client.post(
            "/accounts/login/", {"username": "admin", "password": "admin"}
        )

        self.assertEqual(Trip.objects.count(), 2)
        trip = {
            "name": "Trip to Somewhere",
            "description": "A testing trip",
            "start_date": "2023-06-01",
        }
        response = self.client.post("/create/trip", trip)
        self.assertEqual(Trip.objects.count(), 3)
        self.assertEqual(Trip.objects.get(pk=3).day_set.count(), 1)
        response = self.client.get("")
        self.assertContains(response, "Trip to Somewhere")

    def test_create_day_event(self):
        response = self.client.post(
            "/accounts/login/", {"username": "admin", "password": "admin"}
        )

        trip = Trip.objects.get(pk=1)
        self.assertEqual(trip.day_set.count(), 5)
        response = self.client.get("/add/day/1")
        self.assertEqual(trip.day_set.count(), 6)
        day = trip.day_set.get(num=6)
        self.assertEqual(day.event_set.count(), 0)
        event = {
            "day": day.pk,
            "name": "Ramen",
            "category": "Food",
            "time": "13:00",
            "location": "Restaurant",
            "cost": "20",
            "description": "Good ramen",
        }
        response = self.client.post(f"/create/event/{day.pk}", event)
        self.assertEqual(day.event_set.count(), 1)

    def test_edit_trip(self):
        response = self.client.post(
            "/accounts/login/", {"username": "admin", "password": "admin"}
        )

        response = self.client.get("/view/trip/1")
        self.assertContains(response, "Trip to Barcelona")
        trip = {
            "name": "Trip to Test Change",
            "description": "A 5-day trip to Barcelona, exploring its beautiful architecture and vibrant culture",
            "start_date": "2023-05-10",
        }
        response = self.client.post("/edit/trip/1", trip)
        response = self.client.get("/view/trip/1")
        self.assertContains(response, "Trip to Test Change")

    def test_delete_trip(self):
        response = self.client.post(
            "/accounts/login/", {"username": "admin", "password": "admin"}
        )

        self.assertEqual(Trip.objects.count(), 2)
        self.assertEqual(Event.objects.count(), 28)
        response = self.client.get("/delete/trip/1")
        self.assertEqual(Trip.objects.count(), 1)
        self.assertEqual(Event.objects.count(), 14)
