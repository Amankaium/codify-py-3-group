from django.urls import path, include
from .views import *


urlpatterns = [
    path('category-list/', CategoryList.as_view(), name='category'),
    path('create-product/', CreateProductAPIView.as_view(), name='create-product'),
]