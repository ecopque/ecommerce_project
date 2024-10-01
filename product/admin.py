# FILE: /product/admin.py

from django.contrib import admin
# IMPORT⬇: /product/models.py
from product.models import Product

admin.site.register(Product) ##

# https://linktr.ee/edsoncopque