from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter
from nestedSerializerApp.views import *

router = DefaultRouter()

# router.register()

router.register('author', AuthorViewSet)

router.register('book', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

