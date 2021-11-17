from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render

from firstApp.models import Employee

# Create your views here.
def emp_details(request):
    # emp = Employee(id=1,name='Ruchika', salary = 825)
    # emp.save()

    # emp = Employee(id=2,name='Monica', salary = 800)
    # emp.save()

    data = Employee.objects.all()
    response = {
        'employees': list(data.values('name', 'salary'))
    }

    # emp = {
    #     'id': 123,
    #     'name': 'Ruchika',
    #     'salary': 825000
    # }

    return JsonResponse(response)