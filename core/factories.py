import factory
from .models import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.Sequence(lambda c: f'Test category {c}')
