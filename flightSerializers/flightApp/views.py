from django.shortcuts import render
from rest_framework.decorators import *
from rest_framework.response import Response
from rest_framework import status

from flightApp.models import *
from flightApp.serializers import *

# Create your views here.


@api_view(['POST', 'GET'])
def passenger_list(request):

    if request.method == 'GET':
        passenger_obj = Passenger.objects.all()
        serial_obj = PassengerSerializer(passenger_obj, many=True)
        return Response(serial_obj.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        deserialized_obj = PassengerSerializer(data=request.data)
        if deserialized_obj.is_valid():
            deserialized_obj.save()
            return Response(deserialized_obj.data, status=status.HTTP_201_CREATED)
        return Response(deserialized_obj.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE'])
def passenger_detail(request,p_id):
    
    try:
        psg = Passenger.objects.get(pk=p_id)
    except Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    # get

    if request.method == 'GET':
        return Response(PassengerSerializer(psg).data, status.HTTP_200_OK)

    # update
    elif request.method == 'PUT':
        updated_obj_serializer = PassengerSerializer(psg, data=request.data)
        if updated_obj_serializer.is_valid():
            updated_obj_serializer.save()
            return Response(updated_obj_serializer.data, status=status.HTTP_200_OK)
        return Response(updated_obj_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT
    elif request.method == 'DELETE':
        psg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

        
        
