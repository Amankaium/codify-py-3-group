from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class CategoryList(APIView):
    def get(self, request):
        cat_list = Category.objects.all()
        serializer = CategorySerializer(instance=cat_list, many=True)
        return Response(serializer.data)
