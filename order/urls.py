# FILE: /order/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Pay.as_view(), name='pay'),
    path('close_order', views.Close_Order.as_view(), name='close_order'),
    path('details', views.Details.as_view(), name='details'),
]


# https://linktr.ee/edsoncopque