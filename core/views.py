from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .filters import ProductFilter  # Import the ProductFilter class
from .models import *
from .serializers import *

# Create your views here.
class ProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class CategoryList(APIView):
    def get(self, request):
        cat_list = Category.objects.all()
        serializer = CategorySerializer(instance=cat_list, many=True)
        return Response(serializer.data)


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]


class CreateProductAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs['pk']
        product_object = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product_object)
        return Response(serializer.data)
