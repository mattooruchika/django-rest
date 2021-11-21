from django.shortcuts import render
from django.views.generic.base import View

from rest_framework import viewsets
from nestedSerializerApp.models import *
from nestedSerializerApp.serializer import *

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerailizer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


