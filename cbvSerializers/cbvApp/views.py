from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from cbvApp.models import *
from cbvApp.serializer import *

# Create your views here.
class StudentList(APIView):

    def get(self, request):
        stu = Student.objects.all()
        ser_obj = StudentSerializer(stu, many=True)
        return Response(ser_obj.data, status=status.HTTP_200_OK)

    def post(self, request):
        deserialed_obj = StudentSerializer(data=request.data)
        if deserialed_obj.is_valid():
            deserialed_obj.save()
            return Response(deserialed_obj.data, status=status.HTTP_201_CREATED)
        return Response(deserialed_obj.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):

    def __get_stu_obj(self, stu_id):
        return get_object_or_404(Student,stu_id)

    def get(self, request, stu_id):
        stu = self.__get_stu_obj(stu_id)
        return Response(StudentSerializer(stu).data)

    def delete(self, request, stu_id):
        stu = self.__get_stu_obj(stu_id)
        stu.delete()
        return Response(status.HTTP_204_NO_CONTENT)

    def put(self, request, stu_id):
        stu = self.__get_stu_obj(stu_id)
        deserialized_obj = StudentSerializer(stu, data=request.data)
        if deserialized_obj.is_valid():
            deserialized_obj.save()
            return Response(deserialized_obj.data, status=status.HTTP_200_OK)
        return Response(deserialized_obj.errors, status=status.HTTP_400_BAD_REQUEST)

        





