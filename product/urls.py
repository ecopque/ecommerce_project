#FILE: /product/urls.py

from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.productlist.as_view(), name='list'),
]
