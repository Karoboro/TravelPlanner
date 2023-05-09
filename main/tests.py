from django.db.utils import IntegrityError
from django.test import TestCase
from django.test.utils import setup_test_environment

from .models import Day


# Create your tests here.
class TripModelTests(TestCase):
    def test_number_of_days(self):
        trip = Trip(name="Trip to Somewhere", description="A testing trip")
        trip.save()
        trip.day_set.create(num=1)
        trip.day_set.create(num=2)
        trip.day_set.create(num=3)
        self.assertIs(len(trip), 3)
