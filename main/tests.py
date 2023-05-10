from django.db.utils import IntegrityError
from django.test import TestCase
from django.test.utils import setup_test_environment

from .models import Trip


# Create your tests here.
class TripModelTests(TestCase):
    def setUp(self):
        Trip.objects.create(name="Trip to Somewhere", description="A testing trip")

    def test_number_of_days(self):
        trip = Trip.objects.get(name="Trip to Somewhere")
        trip.day_set.create(num=1)
        trip.day_set.create(num=2)
        trip.day_set.create(num=3)
        self.assertIs(len(trip), 3)

    def test_invalid_duplicate_day(self):
        with self.assertRaises(IntegrityError):
            trip = Trip.objects.get(name="Trip to Somewhere")
            trip.day_set.create(num=1)
            trip.day_set.create(num=1)

    def test_invalid_neg_day_num(self):
        with self.assertRaises(IntegrityError):
            trip = Trip.objects.get(name="Trip to Somewhere")
            trip.day_set.create(num=-1)

    def test_invalid_event_cost(self):
        with self.assertRaises(IntegrityError):
            trip = Trip.objects.get(name="Trip to Somewhere")
            day = trip.day_set.create(num=1)
            day.save()
            day.event_set.create(
                name="Ramen",
                category="Food",
                time="13:00",
                location="Restaurant",
                cost="-10",
                description="Good ramen",
            )
