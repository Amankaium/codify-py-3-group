from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from .models import *
from .serializers import *


class UpdateProductAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer