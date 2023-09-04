from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Category


class TestCategoryTestCase(TestCase):
    def test_model_category_fields(self):
        category_name = "test category 1"
        new_category = Category.objects.create(name=category_name)
        self.assertEqual(new_category.name, category_name)
        self.assertTrue(new_category.id > 0)      
