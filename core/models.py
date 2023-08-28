from django.db import models


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
