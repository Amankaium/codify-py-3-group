import factory
from .models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = "test Category 1"
