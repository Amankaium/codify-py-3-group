import unittest

from django.test import TestCase
from .models import Category


class CategoryTests(unittest.TestCase):
    def setUp(self):
        self.category = Category("Mobile")

    def test_category_name(self):
        self.assertEqual(self.category.name, "")
