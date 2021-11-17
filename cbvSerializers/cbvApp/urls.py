from django.urls import path
from cbvApp.views import *

urlpatterns = [
    path('students/', view=StudentList.as_view()),
    path('students/<int:stu_id>', view=StudentDetail.as_view()),
]
