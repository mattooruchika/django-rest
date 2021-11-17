from django.urls import path
from fbvApp.views import *

urlpatterns = [
    path('students/', view=student_list),
    path('students/<int:stu_id>', view=student_detail),
]
