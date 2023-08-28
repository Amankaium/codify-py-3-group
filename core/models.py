from django.contrib.auth.models import User
from django.db import models


class Purchase(models.Model):
    user = models.ForeignKey(to=User, related_name='buyer', on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True)
    product = models.ManyToManyField(to=Product, related_name='product', blank=False)

    def __str__(self):
        return f'{self.user} - {self.product} - {self.date}'

    class Meta:
        ordering = ['id']
