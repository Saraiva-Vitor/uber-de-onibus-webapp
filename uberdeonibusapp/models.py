from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return self.name

# https://www.google.com.br/maps/@-22.2838797,-42.5370439,16z?entry=ttu
# https://www.google.com.br/maps/@-22.2879963,-42.5354955
# https://www.google.com.br/maps/dir/-22.2878891,-42.5329371/-22.2835792,-42.5311349/data=!4m2!4m1!3e0?entry=ttu

class BusRoute(models.Model):
    name = models.CharField(max_length=100)
    origin = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='origin_routes')
    destination = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='destination_routes')

    def __str__(self):
        return f'{self.name} ({self.origin} to {self.destination})'
