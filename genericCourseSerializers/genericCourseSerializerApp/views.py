from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.
from genericCourseSerializerApp.models import *
from genericCourseSerializerApp.serializer import *

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# Generics 
# class CourseList(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

# class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer