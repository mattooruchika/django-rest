from consumerOrderSerializerApp.models import *
from rest_framework.serializers import ModelSerializer


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ConsumerSerializer(ModelSerializer):
    orders = OrderSerializer(read_only=True, many=True)
    class Meta:
        model = Consumer
        fields = '__all__'

