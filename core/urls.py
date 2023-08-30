from django.urls import path, include
from .views import *


urlpatterns = [
    path('category-list/', CategoryList.as_view(), name='category'),
    path('create-product/', CreateProductAPIView.as_view(), name='create-product'),
    path('product-info/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),
    path('products/', ProductsListAPIView.as_view(), name='products'),
]