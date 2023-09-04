from django.test import TestCase
from rest_framework.test import APITestCase
from .factories import CategoryFactory
from .models import Category
class CategoriesTest(APITestCase):
    def setUp(self):
        self.cate = CategoryFactory()

    def test_get_list_of_categories(self):
        response = self.client.get('/category-list/')
        self.assertEqual(response.status_code, 200)


    #def test_get_one_categorie(self):
       # response = self.client.get(f'/category/{self.cate.pk}/')
       # self.assertEqual(response.status_code, 200)