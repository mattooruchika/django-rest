from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    ratings = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])



