#FILE: /product/urls.py

from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # IMPORT⬇: /product/views.py
    path('', views.ProductList.as_view(), name='list'), #1:
    path('<slug>', views.ProductDetail.as_view(), name='detail'), #2:
    path('addtocart/', views.AddToCart.as_view(), name='addtocart'),
    path('removefromcart/', views.RemoveFromCart.as_view(), name='removefromcart'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('purchasesummary/', views.PurchaseSummary.as_view(), name='purchasesummary'),
    path('search/', views.Search.as_view(), name='search'),
]


# ------------------------------------------------------------------
#1: Essa linha define a rota para a URL raiz ('') do aplicativo product. Ela está associada à view ProductList no arquivo /product/views.py. O método as_view() é usado porque ProductList é uma classe baseada em view (ListView), o que converte a classe em uma view que pode responder a requisições HTTP. O nome dessa URL é list.
#2: Essa rota aceita uma parte variável da URL representada por <slug>. Ela está associada à view ProductDetail no arquivo /product/views.py. O parâmetro slug será passado para a view, permitindo que ele busque e mostre detalhes de um produto específico. O nome dessa URL é detail.

# https://linktr.ee/edsoncopque