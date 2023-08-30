from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
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


class ProductAPIView(APIView):
    def get(request, pk):
        product_object = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product_object)
        return Response(serializer.data, safe=False)
