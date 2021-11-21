from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name+" "+self.last_name

class Book(models.Model):
    title = models.CharField(max_length=20)
    ratings = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
