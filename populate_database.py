import os

import django
from django.contrib.auth.models import User
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TravelPlanner.settings")
django.setup()

from main.models import Day, Event, Trip


def add_trip(name, description):
    trip = Trip(name=name, description=description)
    trip.user = User.objects.get(pk=1)
    trip.save()
    return trip


def add_day(trip, num):
    day = Day(trip=trip, num=num)
    day.save()
    return day


def add_event(day, name, category, time, location, cost, description):
    event = Event(
        day=day,
        name=name,
        category=category,
        time=time,
        location=location,
        cost=cost,
        description=description,
    )
    event.save()


def populate_data():
    trip = add_trip(
        "Trip to Barcelona",
        "A 5-day trip to Barcelona, exploring its beautiful architecture and vibrant culture",
    )

    day1 = add_day(trip, 1)
    add_event(
        day1,
        "Visit La Sagrada Familia",
        "Entertainment",
        "10:00",
        "La Sagrada Familia, Barcelona",
        25,
        "Visit the world-famous La Sagrada Familia, designed by architect Antoni Gaudí",
    )
    add_event(
        day1,
        "Lunch at Can Solé",
        "Food",
        "13:00",
        "Can Solé, Barcelona",
        30,
        "Enjoy a delicious Spanish lunch at Can Solé, a popular local seafood restaurant",
    )
    add_event(
        day1,
        "Explore Park Güell",
        "Entertainment",
        "16:00",
        "Park Güell, Barcelona",
        10,
        "Discover Park Güell, another masterpiece designed by Antoni Gaudí",
    )

    day2 = add_day(trip, 2)
    add_event(
        day2,
        "Visit Casa Batlló",
        "Entertainment",
        "10:00",
        "Casa Batlló, Barcelona",
        25,
        "Experience the beautiful architecture of Casa Batlló, designed by Antoni Gaudí",
    )
    add_event(
        day2,
        "Lunch at Bar Cañete",
        "Food",
        "13:00",
        "Bar Cañete, Barcelona",
        35,
        "Enjoy a delicious Spanish lunch at Bar Cañete, a popular local tapas bar",
    )
    add_event(
        day2,
        "Visit Picasso Museum",
        "Entertainment",
        "15:00",
        "Picasso Museum, Barcelona",
        15,
        "Explore the extensive collection of artworks by Pablo Picasso at the Picasso Museum",
    )

    day3 = add_day(trip, 3)
    add_event(
        day3,
        "Visit Camp Nou",
        "Entertainment",
        "10:00",
        "Camp Nou, Barcelona",
        30,
        "Take a tour of Camp Nou, the iconic stadium of FC Barcelona",
    )
    add_event(
        day3,
        "Lunch at Cervecería Catalana",
        "Food",
        "13:00",
        "Cervecería Catalana, Barcelona",
        30,
        "Enjoy a delicious Spanish lunch at Cervecería Catalana, a popular local tapas bar",
    )
    add_event(
        day3,
        "Explore La Rambla",
        "Entertainment",
        "15:00",
        "La Rambla, Barcelona",
        0,
        "Stroll down the famous La Rambla, a bustling pedestrian street with shops, cafes, and street performers",
    )

    day4 = add_day(trip, 4)
    add_event(
        day4,
        "Check in at Hotel Arts Barcelona",
        "Accommodation",
        "12:00",
        "Hotel Arts Barcelona",
        200,
        "Enjoy a luxurious stay at Hotel Arts Barcelona with a beautiful view of the city",
    )
    add_event(
        day4,
        "Take a metro to the Magic Fountain of Montjuïc",
        "Transportation",
        "18:00",
        "Barcelona Metro",
        5,
        "Experience the efficient metro system of Barcelona",
    )
    add_event(
        day4,
        "Visit Magic Fountain of Montjuïc",
        "Entertainment",
        "20:00",
        "Magic Fountain of Montjuïc, Barcelona",
        0,
        "Enjoy a spectacular display of color, light, motion, music and water acrobatics",
    )

    day5 = add_day(trip, 5)
    add_event(
        day5,
        "Take a taxi to the airport",
        "Transportation",
        "10:00",
        "Barcelona Airport",
        30,
        "Return journey to the airport",
    )
    add_event(
        day5,
        "Buy souvenirs at Duty Free",
        "Misc",
        "12:00",
        "Barcelona Airport",
        100,
        "Get some souvenirs and gifts for your loved ones at Duty Free",
    )

    trip_japan = add_trip(
        "Trip to Japan",
        "A 3-day trip to Japan, exploring its rich history and vibrant culture",
    )

    day1_japan = add_day(trip_japan, 1)
    add_event(
        day1_japan,
        "Visit Senso-ji Temple",
        "Entertainment",
        "10:00",
        "Senso-ji Temple, Tokyo",
        10,
        "Visit the oldest temple in Tokyo, Senso-ji Temple, located in the Asakusa district",
    )
    add_event(
        day1_japan,
        "Lunch at Sushi Dai",
        "Food",
        "13:00",
        "Sushi Dai, Tokyo",
        50,
        "Enjoy an authentic sushi experience at Sushi Dai, a famous sushi restaurant in Tsukiji Fish Market",
    )
    add_event(
        day1_japan,
        "Explore Akihabara",
        "Entertainment",
        "15:00",
        "Akihabara, Tokyo",
        0,
        "Discover the vibrant Akihabara district, known for its electronics, gaming, and anime culture",
    )

    day2_japan = add_day(trip_japan, 2)
    add_event(
        day2_japan,
        "Visit Meiji Shrine",
        "Entertainment",
        "10:00",
        "Meiji Shrine, Tokyo",
        0,
        "Explore the serene Meiji Shrine, dedicated to the deified spirits of Emperor Meiji and Empress Shoken",
    )
    add_event(
        day2_japan,
        "Lunch at Tonkatsu Maisen",
        "Food",
        "13:00",
        "Tonkatsu Maisen, Tokyo",
        25,
        "Savor delicious tonkatsu at Tonkatsu Maisen, a renowned tonkatsu restaurant in Tokyo",
    )
    add_event(
        day2_japan,
        "Visit Odaiba",
        "Entertainment",
        "15:00",
        "Odaiba, Tokyo",
        20,
        "Enjoy the sights and attractions of Odaiba, a popular shopping and entertainment district on a man-made island in Tokyo Bay",
    )

    day3_japan = add_day(trip_japan, 3)
    add_event(
        day3_japan,
        "Visit Ueno Park",
        "Entertainment",
        "10:00",
        "Ueno Park, Tokyo",
        0,
        "Stroll through Ueno Park, a spacious public park featuring museums, a zoo, and several major temples and shrines",
    )
    add_event(
        day3_japan,
        "Lunch at Ramen Street",
        "Food",
        "13:00",
        "Tokyo Ramen Street, Tokyo",
        15,
        "Try some of the best ramen in Tokyo at Tokyo Ramen Street, located in the basement of Tokyo Station",
    )
    add_event(
        day3_japan,
        "Explore Shibuya Crossing",
        "Entertainment",
        "15:00",
        "Shibuya Crossing, Tokyo",
        0,
        "Witness the world-famous Shibuya Crossing, one of the busiest pedestrian intersections in the world",
    )

    day4_japan = add_day(trip_japan, 4)
    add_event(
        day4_japan,
        "Check in at The Ritz-Carlton, Tokyo",
        "Accommodation",
        "14:00",
        "The Ritz-Carlton, Tokyo",
        350,
        "Stay at The Ritz-Carlton, Tokyo, an opulent hotel offering a stunning view of the city",
    )
    add_event(
        day4_japan,
        "Take a metro to Roppongi Hills",
        "Transportation",
        "16:00",
        "Tokyo Metro",
        3,
        "Navigate through Tokyo's comprehensive metro system",
    )
    add_event(
        day4_japan,
        "Explore Roppongi Hills",
        "Entertainment",
        "17:00",
        "Roppongi Hills, Tokyo",
        0,
        "Experience the modern side of Tokyo at Roppongi Hills, a complex with shops, restaurants, and a museum",
    )

    day5_japan = add_day(trip_japan, 5)
    add_event(
        day5_japan,
        "Take a taxi to the airport",
        "Transportation",
        "10:00",
        "Narita International Airport",
        50,
        "Return journey to the airport",
    )
    add_event(
        day5_japan,
        "Buy souvenirs at Duty Free",
        "Misc",
        "12:00",
        "Narita International Airport",
        100,
        "Get some souvenirs and gifts for your loved ones at Duty Free",
    )


if __name__ == "__main__":
    populate_data()
