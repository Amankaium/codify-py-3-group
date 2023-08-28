from rest_framework.serializers import ModelSerializer
from .models import *


class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
