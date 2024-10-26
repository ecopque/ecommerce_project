# FILE: /order/urls.py

from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.Pay.as_view(), name='pay'),
    path('save_order/', views.SaveOrder.as_view(), name='save_order'),
    path('list/', views.List.as_view(), name='list'),
    path('details/', views.Details.as_view(), name='details'),
]


# https://linktr.ee/edsoncopque