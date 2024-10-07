#FILE: /product/urls.py

from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # IMPORT⬇: /product/views.py
    path('', views.ProductList.as_view(), name='list'),
]
