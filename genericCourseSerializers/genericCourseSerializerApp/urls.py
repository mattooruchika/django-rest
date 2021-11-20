from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from genericCourseSerializerApp.views import *

router = DefaultRouter()
router.register('course', CourseViewSet)

# for viewset
urlpatterns = [
    path('', include(router.urls)),
]



# GENERICS
# urlpatterns = [
#     path('course/', view=CourseList.as_view()),
#     path('course/<int:pk>', view=CourseDetail.as_view()),
# ]
