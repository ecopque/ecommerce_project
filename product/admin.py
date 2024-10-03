# FILE: /product/admin.py

from django.contrib import admin
# IMPORT⬇: /product/models.py
from product.models import Product, Variation


class VariationInLine(admin.TabularInline): ##
    model = Variation ##
    extra = 3 ##

#URL⬇: http://127.0.0.1:8000/admin/product/product/add/
class ProductAdmin(admin.ModelAdmin): ##
    inlines = [VariationInLine] ##

admin.site.register(Product, ProductAdmin) ##
admin.site.register(Variation) ##

string = 'That\'s a nice idea'
# https://linktr.ee/edsoncopque