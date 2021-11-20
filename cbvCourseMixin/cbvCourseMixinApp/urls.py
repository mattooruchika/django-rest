from django.urls import path
from cbvCourseMixinApp.views import *

urlpatterns = [
    path('course/', view=CourseList.as_view()),
    path('course/<int:pk>', view=CourseDetail.as_view()),
]
