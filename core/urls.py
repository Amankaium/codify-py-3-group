from django.urls import path, include
from .views import *


urlpatterns = [
    path('category-list/', CategoryList.as_view(), name='category'),
    path('purchase-list/', PurchaseViewSet.as_view({'get': 'list'})),
    path('purchase-update/<int:pk>/', PurchaseViewSet.as_view({'put': 'update'})),
    path('purchase-patch/<int:pk>/', PurchaseViewSet.as_view({'patch': 'partial_update'})),
    path('purchase-create/', PurchaseViewSet.as_view({'post': 'create'})),
    path('create-product/', CreateProductAPIView.as_view(), name='create-product'),
    path('product-info/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),
    path('products/', ProductsListAPIView.as_view(), name='products'),
]
