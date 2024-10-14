from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

class Variant(models.Model):
    products = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    details = models.TextField
    