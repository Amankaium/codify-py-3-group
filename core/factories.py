import factory
from .models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(
        lambda n: f'Test category {n}'
    )

