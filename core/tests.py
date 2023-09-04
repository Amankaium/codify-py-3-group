from django.test import TestCase
from rest_framework.test import APITestCase
from .factories import CategoryFactory

class CategoryListTest(TestCase):
    def test_open_category_should_success(self):

        response = self.client.get('/category-list/')
        assert response.status_code == 200


class CategoryTestCase(APITestCase):
    def test_get_list_of_categorys(self):

        category_1 = CategoryFactory()
        category_2 = CategoryFactory()
        category_3 = CategoryFactory()
        response = self.client.get('/category-list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(category_1.name, response.data[0]["name"])
        self.assertEqual(category_2.name, response.data[1]["name"])
        self.assertEqual(category_3.name, response.data[2]["name"])

