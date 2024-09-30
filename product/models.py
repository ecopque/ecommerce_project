# FILE: product/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='product_images/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True)
    marketing_price = models.FloatField()
    promotional_marketing_price = models.FloatField(default=0)
    type = models.CharField(default='V', max_length=1, choices=(
        ('V', 'Variation'),
        ('S', 'Simple'),
        ),
    )


# https://linktr.ee/edsoncopque