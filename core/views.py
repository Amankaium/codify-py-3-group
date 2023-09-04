from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .filters import ProductFilter

from .models import *
from .serializers import *

class ProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class CategoryList(APIView):
    def get(self, request):
        cat_list = Category.objects.all()
        serializer = CategorySerializer(instance=cat_list, many=True)
        return Response(serializer.data)


class UpdateProductAPIView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        product_object = Product.objects.get(pk=pk)
        data = request.data
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            product_object.name = serializer.validated_data["name"]
            product_object.price = serializer.validated_data["price"]
            product_object.category = serializer.validated_data["category"]
            product_object.save()

            serializer = ProductSerializer(instance=product_object)

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

