from .models import Driver, BusType, Bus, Location, BusRoute, Profiles
from django.contrib import admin

admin.site.register(Location)
admin.site.register(BusRoute)
admin.site.register(Driver)
admin.site.register(BusType)
admin.site.register(Bus)
admin.site.register(Profiles)
