import factory
from .models import Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(
        lambda n: f'Test category {n}'
    )

    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    name = factory.Sequence(
        lambda n: f'Test Product {n}'
    )
    price = 100
    category = factory.SubFactory(CategoryFactory)
