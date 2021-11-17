from django.urls import path
from django.urls.conf import include

from firstApp.views import *

urlpatterns = [
    path('emp/', emp_details),
]
