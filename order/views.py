# FILE: /order/views.py

from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

class Pay(ListView):
    ...

class SaveOrder(View):
    ...

class Details(View):
    ...


# https://linktr.ee/edsoncopque