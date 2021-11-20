from django.urls import path
from cbvStudentApp.views import *

urlpatterns = [
    path('students/', view=StudentList.as_view()),
    path('students/<int:pk>', view=StudentDetail.as_view()),
]
