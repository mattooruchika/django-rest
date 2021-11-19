from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cbvCourseApp.models import Course
from cbvCourseApp.serializers import CourseSerializer

# Create your views here.

class CourseList(APIView):

    def get(self, request):
        courses = Course.objects.all()

        return Response(CourseSerializer(courses, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        desrialized_course_obj = CourseSerializer(data=request.data)
        if desrialized_course_obj.is_valid():
            desrialized_course_obj.save()
            return Response(desrialized_course_obj.data, status=status.HTTP_201_CREATED)
        return Response(desrialized_course_obj.errors, status=status.HTTP_400_BAD_REQUEST)



class CourseDetail(APIView):

    def __get_course_object(self, course_id):
        return get_object_or_404(Course,course_id)

    def get(self, request, course_id):
        obj = self.__get_course_object(course_id)
        return Response(CourseSerializer(obj).data, status=status.HTTP_200_OK)

    def put(self, request,course_id ):
        obj = self.__get_course_object(course_id)
        desrialized_course_obj = CourseSerializer(obj, data=request.data)
        if desrialized_course_obj.is_valid():
            desrialized_course_obj.save()
            return Response(desrialized_course_obj.data, status=status.HTTP_200_OK)
        return Response(desrialized_course_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,course_id):
        obj = self.__get_course_object(course_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
