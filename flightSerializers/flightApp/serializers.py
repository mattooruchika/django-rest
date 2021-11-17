
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from flightApp.models import *

class PassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'travel_points']

