from rest_framework.viewsets import ModelViewSet
from consumerOrderSerializerApp.models import *
from consumerOrderSerializerApp.serializer import *
from consumerOrderSerializerApp.views import *


class ConsumerViewSet(ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Create your views here.
