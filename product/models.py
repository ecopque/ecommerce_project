# FILE: /product/models.py

from django.db import models
from PIL import Image ##
import os
from django.conf import settings ##


class Product(models.Model): ##
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

    @staticmethod ##
    def resize_image(img, new_width=800): ##
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name) ##
        print(img_full_path)

    def save(self, *args, **kwargs): ##
        super().save(*args, **kwargs) ##

        max_image_size = 800
        if self.image: ##
            self.resize_image(self.image, max_image_size) ##

    def __str__(self):
        return self.name ##
    


# https://linktr.ee/edsoncopque