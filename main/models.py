from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Trip(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Day(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    num = models.IntegerField(default=1, validators=[MinValueValidator(0)])


class Event(models.Model):
    CATEGORY_LIST = [
        ("Accommodation", "Accommodation"),
        ("Transportation", "Transportation"),
        ("Entertainment", "Entertainment"),
        ("Food", "Food"),
    ]
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY_LIST)
    time = models.TimeField("Start Time")
    location = models.CharField(max_length=200)
    cost = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    description = models.CharField(max_length=200)
