from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Consumer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = PhoneNumberField()

    def __str__(self):
        return self.first_name+" "+self.last_name

class Order(models.Model):
    product = models.CharField(max_length=20)
    quantity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    consumer = models.ForeignKey(Consumer, related_name= "orders",on_delete=models.CASCADE)

    def __str__(self):
        return self.product

