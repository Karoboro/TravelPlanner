import os
import django
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TravelPlanner.settings')
django.setup()

from main.models import Trip, Day, Event

def add_trip(name, description):
    trip = Trip(name=name, description=description)
    trip.save()
    return trip

def add_day(trip, num):
    day = Day(trip=trip, num=num)
    day.save()
    return day

def add_event(day, name, category, time, location, cost, description):
    event = Event(day=day, name=name, category=category, time=time, location=location, cost=cost, description=description)
    event.save()

def populate_data():
    trip = add_trip("Trip to Barcelona", "A 3-day trip to Barcelona, exploring its beautiful architecture and vibrant culture")

    day1 = add_day(trip, 1)
    add_event(day1, "Visit La Sagrada Familia", "Entertainment", "10:00", "La Sagrada Familia, Barcelona", 25, "Visit the world-famous La Sagrada Familia, designed by architect Antoni Gaudí")
    add_event(day1, "Lunch at Can Solé", "Food", "13:00", "Can Solé, Barcelona", 30, "Enjoy a delicious Spanish lunch at Can Solé, a popular local seafood restaurant")
    add_event(day1, "Explore Park Güell", "Entertainment", "16:00", "Park Güell, Barcelona", 10, "Discover Park Güell, another masterpiece designed by Antoni Gaudí")

    day2 = add_day(trip, 2)
    add_event(day2, "Visit Casa Batlló", "Entertainment", "10:00", "Casa Batlló, Barcelona", 25, "Experience the beautiful architecture of Casa Batlló, designed by Antoni Gaudí")
    add_event(day2, "Lunch at Bar Cañete", "Food", "13:00", "Bar Cañete, Barcelona", 35, "Enjoy a delicious Spanish lunch at Bar Cañete, a popular local tapas bar")
    add_event(day2, "Visit Picasso Museum", "Entertainment", "15:00", "Picasso Museum, Barcelona", 15, "Explore the extensive collection of artworks by Pablo Picasso at the Picasso Museum")

    day3 = add_day(trip, 3)
    add_event(day3, "Visit Camp Nou", "Entertainment", "10:00", "Camp Nou, Barcelona", 30, "Take a tour of Camp Nou, the iconic stadium of FC Barcelona")
    add_event(day3, "Lunch at Cervecería Catalana", "Food", "13:00", "Cervecería Catalana, Barcelona", 30, "Enjoy a delicious Spanish lunch at Cervecería Catalana, a popular local tapas bar")
    add_event(day3, "Explore La Rambla", "Entertainment", "15:00", "La Rambla, Barcelona", 0, "Stroll down the famous La Rambla, a bustling pedestrian street with shops, cafes, and street performers")

if __name__ == '__main__':
    populate_data()
