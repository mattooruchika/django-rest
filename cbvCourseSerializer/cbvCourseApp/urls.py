from django.urls import path
from cbvCourseApp.views import *

urlpatterns = [
    path('course/', view=CourseList.as_view()),
    path('course/<int:course_id>', view=CourseDetail.as_view()),
]
