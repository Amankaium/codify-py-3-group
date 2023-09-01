from django.urls import path, include
from .views import *


urlpatterns = [
    path('category-list/', CategoryList.as_view(), name='category'),
    path('update-product/<int:pk>/', UpdateProductAPIView.as_view(), name='update-product'),
]