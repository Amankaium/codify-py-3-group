from django.test import TestCase
from rest_framework.test import APITestCase
from .factories import CategoryFactory, ProductFactory


class ProductTest(APITestCase):
    def setUp(self):
        self.prod_1 = ProductFactory()
        self.prod_2 = ProductFactory()
        self.prod_3 = ProductFactory()

    def test_get_list_of_3_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.prod_1.name, response.data[0]["name"])
        self.assertEqual(self.prod_2.name, response.data[1]["name"])
        self.assertEqual(self.prod_3.name, response.data[2]["name"])

    def test_get_one_collection(self):
        response = self.client.get(f'/product-info/{self.prod_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.prod_1.name, response.data["name"])
        self.assertEqual(self.prod_1.price, response.data["price"])
        self.assertEqual(self.prod_1.category.pk, response.data["category"])
