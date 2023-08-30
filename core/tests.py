from django.test import TestCase
from rest_framework.test import APITestCase
from .factories import ProductFactory


class ProductTest(APITestCase):
    def setUp(self):
        self.prod = ProductFactory()

    def test_get_one_product(self):
        response = self.client.get(f'/product-info/{self.prod.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.prod.name, response.data["name"])

