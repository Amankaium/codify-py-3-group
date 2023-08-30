from django.contrib import admin
from .models import Category, Product, Purchase


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Purchase)
