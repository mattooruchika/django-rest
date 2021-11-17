from django.db import models
from django.db.models.base import Model

# Create your models here.

class Employee(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self) -> str:
        return self.name
