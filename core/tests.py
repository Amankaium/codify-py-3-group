from rest_framework.test import APITestCase
from .factories import ProductFactory
class ProductTestCase(APITestCase):
    def setUp(self):
        self.product_1 = ProductFactory()
        self.product_2 = ProductFactory()
        self.product_3 = ProductFactory()

    def test_get_list_of_3_collections(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.product_1.name, response.data[0]["name"])
        self.assertEqual(self.product_2.name, response.data[1]["name"])
        self.assertEqual(self.product_3.name, response.data[2]["name"])
