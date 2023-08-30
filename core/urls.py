from django.urls import path, include
from .views import *


urlpatterns = [
    path('category-list/', CategoryList.as_view(), name='category'),
    path('update-product/', UpdateProductAPIView.as_view(), name='update-product')
    # для получения доступа к конкретному объекту по id, в конце адресной строки добавляем
    # ?id=1.  Т.е.  http://127.0.0.1:8000/update-product/?id=1
]