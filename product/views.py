# FILE: /product/views.py

from django.shortcuts import render
from django.views.generic.list import ListView ##
from django.views import View ##

class ProductList(ListView): ##
    ...

class ProductDetail(View): ##
    ...

class AddToCart(View): ##
    ...

class RemoveFromCart(View): ##
    ...