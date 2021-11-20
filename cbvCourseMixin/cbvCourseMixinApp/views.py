from django.shortcuts import render

from rest_framework import generics, mixins, serializers
from cbvCourseMixinApp.models import *
from cbvCourseMixinApp.serializers import *

# Create your views here.


class CourseList(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)


class CourseDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get(self, request,pk):
        return self.retrieve(request,pk)
    
    def put(self, request, pk):
        return self.update(request,pk)

    def delete(self, request, pk):
        return self.destroy(request,pk)
