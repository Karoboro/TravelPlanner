from django.contrib import admin

from .models import Day, Event, Trip

# Register your models here.
admin.site.register(Trip)
admin.site.register(Day)
admin.site.register(Event)
