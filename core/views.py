from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView

from .models import *
from .serializers import *

class CategoryList(APIView):
    def get(self, request):
        cat_list= Category.objects.all()
        serializer = CategorySerializer(instance=cat_list, many=True)
        return Response(serializer.data)



class UpdateProductAPIView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        try:
            id = request.query_params["id"]
            if id != None:
                product = Product.objects.get(id=id)
                serializer = ProductSerializer(product)
        except:
            products = self.get_queryset()
            serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        product_object = Product.objects.get(id=id)

        data = request.data

        product_object.name = data["name"]
        product_object.price = data["price"]
        product_object.category = data["category"]

        product_object.save()

        serializer = ProductSerializer(product_object)
        return Response(serializer.data)
