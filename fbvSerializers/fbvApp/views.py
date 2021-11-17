from django.shortcuts import render
from fbvApp.models import *
from fbvApp.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        stu = Student.objects.all()
        serializerobj = StudentSerializer(stu, many=True)
        return Response(serializerobj.data)

    elif request.method == 'POST':
        serializerobj = StudentSerializer(data=request.data)
        if serializerobj.is_valid():
            serializerobj.save()
            return Response(serializerobj.data, status=status.HTTP_201_CREATED)
        return Response(serializerobj.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def student_detail(request, stu_id):
    try:
        stu = Student.objects.get(pk=stu_id)
    except Student.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(StudentSerializer(stu).data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        new_student_serializer = StudentSerializer(stu, data=request.data)
        if new_student_serializer.is_valid():
            new_student_serializer.save()
            return Response(new_student_serializer.data, status=status.HTTP_200_OK)
        return Response(new_student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        


    