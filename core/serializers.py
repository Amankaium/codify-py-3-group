from rest_framework.serializers import ModelSerializer
from .models import *


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
