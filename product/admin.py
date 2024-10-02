# FILE: /product/admin.py

from django.contrib import admin
# IMPORT⬇: /product/models.py
from product.models import Product, Variation

admin.site.register(Product) ##
admin.site.register(Variation) ##

# https://linktr.ee/edsoncopque