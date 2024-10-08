# FILE: /order/views.py

from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

class Pay(ListView):
    ...

class Close_Order(View):
    ...

class Details(View):
    ...