from django.db import models

# Create your models here.

class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    travel_points = models.IntegerField()

    def __str__(self) -> str:
        return self.first_name+self.last_name
