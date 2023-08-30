from django.urls import path, include
from .views import *


urlpatterns = [
    path('category-list/', CategoryList.as_view(), name='category'),
    path('products/', ProductsListAPIView.as_view(), name='products'),
]