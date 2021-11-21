

from rest_framework.routers import DefaultRouter

from consumerOrderSerializerApp.views import *



router = DefaultRouter()


router.register('order', OrderViewSet)

router.register('consumer', ConsumerViewSet)

from django.urls import path, include


urlpatterns = [
    path('', include(router.urls)),
]