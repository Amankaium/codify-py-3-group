from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

# Create your views here.
class ProductsListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter