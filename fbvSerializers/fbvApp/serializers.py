from django.db.models import fields
from rest_framework import serializers
from fbvApp.models import *



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'score']

