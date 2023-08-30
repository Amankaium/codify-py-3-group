import factory
from .models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = "test Category 1"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    name = "Test Product 1"
    price = "200"
