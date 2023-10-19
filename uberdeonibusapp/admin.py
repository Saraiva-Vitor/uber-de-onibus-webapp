from django.contrib import admin

from .models import Location, BusRoute

admin.site.register(Location)
admin.site.register(BusRoute)
