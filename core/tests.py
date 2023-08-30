from django.test import TestCase

from .models import Category


class CategoryTestCase(TestCase):
    def test_open_category_should_success(self):

        response = self.client.get('/category-list/')
        assert response.status_code == 200

