# from django.contrib.auth.models import User
from datetime import date

from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start_date = models.DateField("Start Date", default=date.today)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __len__(self):
        return self.day_set.count()


class Day(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(num__gte=1), name="num_gte_1"),
            models.UniqueConstraint(fields=["trip", "num"], name="unique_day"),
        ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    num = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.num)

    def __len__(self):
        return self.event_set.count()


class Event(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(cost__gte=0), name="cost_gte_0")
        ]

    CATEGORY_LIST = [
        ("Accommodation", "Accommodation"),
        ("Transportation", "Transportation"),
        ("Entertainment", "Entertainment"),
        ("Food", "Food"),
        ("Misc", "Misc"),
    ]
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY_LIST)
    time = models.TimeField("Start Time")
    location = models.CharField(max_length=200)
    cost = models.FloatField(default=0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length=200)

    def __str__(self):
        return (
            f"<{self.category}> {self.name} - {self.time} {self.location} {self.cost}"
        )
