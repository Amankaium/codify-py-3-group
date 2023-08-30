from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class CategoryList(APIView):
    def get(self, request):
        cat_list= Category.objects.all()
        serializer = CategorySerializer(instance=cat_list, many=True)
        return Response(serializer.data)



class UpdateProductAPIView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        product_object = Product.objects.get(pk=pk)

        data = request.data

        product_object.name = data["name"]
        product_object.price = data["price"]
        product_object.category = data["category"]

        product_object.save()

        serializer = ProductSerializer(product_object)
        return Response(serializer.data)
