from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class BusRoute(models.Model):
    name = models.CharField(max_length=100)
    origin = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='origin_routes')
    destination = models.ForeignKey(
        Location, on_delete=models.CASCADE, related_name='destination_routes')

    def __str__(self):
        return f'{self.name} ({self.origin} to {self.destination})'
