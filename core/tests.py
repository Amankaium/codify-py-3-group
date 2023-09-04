from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Category
from .factories import CategoryFactory, ProductFactory


class ProductTest(APITestCase):
    def setUp(self):
        self.prod = ProductFactory()

    def test_get_one_product(self):
        response = self.client.get(f'/product-info/{self.prod.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.prod.name, response.data["name"])


class TestCategoryTestCase(TestCase):
    def test_model_category_fields(self):
        category_name = "test category 1"
        new_category = Category.objects.create(name=category_name)
        self.assertEqual(new_category.name, category_name)
        self.assertTrue(new_category.id > 0)      


class ProductsTest(APITestCase):
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
