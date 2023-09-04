import factory
from .models import Category, Product, Purchase
from django.contrib.auth.models import User
from datetime import date


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "test Category 1"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(
        lambda n: f'Test Product {n}'
    )
    price = 100
    category = factory.SubFactory(CategoryFactory)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(
        lambda n: f'test_user_{n}'
    )


class PurchaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Purchase

    user = factory.SubFactory(UserFactory)
    date = factory.LazyFunction(date.today)
