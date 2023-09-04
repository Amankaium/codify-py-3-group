from django.test import TestCase
from rest_framework.test import APITestCase
from .factories import *
from .models import *


class ProductUpdateTest(APITestCase):
    def setUp(self):
        self.product_data = ProductFactory()
    def test_put_product(self):
        new_data = {
            "name": "phone 14",
            "price": 2220,
            "category": 1
        }
        response = self.client.put(f'/update-product/{self.product_data.pk}/', data=new_data)
        self.assertEqual(response.status_code, 200)

        updated_product = Product.objects.get(pk=self.product_data.pk)
        self.assertEqual(updated_product.name, new_data['name'])
        self.assertEqual(updated_product.price, new_data['price'])
        self.assertEqual(updated_product.category.pk, new_data['category'])

