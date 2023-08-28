from django.contrib.auth.models import User
from django.db import models


class Purchase(models.Model):
    user = models.ForeignKey(to=User, related_name='buyer', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    product = models.ManyToManyField(to='Product', related_name='product', blank=False)

    def __str__(self):
        return f'{self.user} - {self.product.name} - {self.date}'

    class Meta:
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name

