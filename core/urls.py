from rest_framework import routers
from django.urls import path, include
from .views import *


category_router = routers.DefaultRouter()
category_router.register(r'', CategoryViewSet)


urlpatterns = [
    path('category/', CategoryViewSet.as_view(), name='category'),
    path('', include(category_router.urls)),
]