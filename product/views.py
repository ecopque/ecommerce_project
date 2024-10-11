# FILE: /product/views.py

from django.shortcuts import render
from django.views.generic.list import ListView ##
from django.views import View ##
from . import models

# IMPORT⬇: /product/models.py
class ProductList(ListView): ##
    model = models.Product ##
    template_name = 'product/list.html' ##
    context_object_name = 'products' ##
    paginate_by = 3 ##

class ProductDetail(View): ##
    ...

class AddToCart(View): ##
    ...

class RemoveFromCart(View): ##
    ...

class Cart(View): ##
    ...

class Finish(View): ##
    ...


# https://linktr.ee/edsoncopque