from rest_framework.generics import CreateAPIView
from .models import *
from .serializers import *


class CreateProductAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



