# FILE: /product/views.py

from django.shortcuts import render
from django.views.generic.list import ListView #1:
from django.views import View #2:
from . import models
from django.views.generic.detail import DetailView #8:

class ProductList(ListView): #3:
    # IMPORT⬇: /product/models.py
    model = models.Product #4:

    template_name = 'product/list.html' #5:
    context_object_name = 'products' #6:
    paginate_by = 3 #7:

class ProductDetail(DetailView): #9:
    model = models.Product
    template_name = 'product/detail.html'
    context_object_name = 'product'

    #IMPORT⬇: /product/urls.py
    slug_url_kwarg = 'slug' #10:

class AddToCart(View):
    ...

class RemoveFromCart(View):
    ...

class Cart(View):
    ...

class Finish(View):
    ...


# ------------------------------------------------------------------
#8: Essa classe é uma view genérica fornecida pelo Django que facilita a exibição de detalhes de um objeto específico. No código, DetailView é usada na classe ProductDetail para mostrar os detalhes de um produto.
#9: A classe ProductDetail herda de DetailView, o que significa que ela é usada para exibir os detalhes de um objeto específico, no caso, um produto. O Django usa essa classe para buscar o objeto no banco de dados, renderizar o template especificado e fornecer o contexto para o template.
#10: Esse atributo especifica o nome do parâmetro na URL que será usado para procurar o objeto. Aqui, o parâmetro 'slug' na URL será utilizado para buscar o produto correspondente no banco de dados. A configuração geralmente é feita no arquivo urls.py para mapear a URL a essa view.
# ------------------------------------------------------------------
#1: Importa a classe ListView de django.views.generic.list. ListView é uma class-based view que renderiza uma lista de objetos. Essa classe é usada para facilitar a exibição de listas no Django.
#2: Importa a classe base View de django.views. View é a classe mais básica para todas as class-based views no Django.
#3: Define a view ProductList, que herda de ListView. Isso permite a exibição de uma lista de produtos da base de dados no template. A classe ProductList serve para exibir uma lista de produtos através de um queryset, que será passado para o contexto do template.
#4: Define o modelo Product (da pasta /product/models.py) que será utilizado pela ProductList para carregar os dados a serem exibidos.
#5: Especifica o template 'product/list.html' para renderizar a lista de produtos. Lógica: Indica qual arquivo HTML será renderizado ao acessar essa view.
#6: Define o nome do contexto que será passado ao template. Nesse caso, a lista de produtos será acessível pelo nome products dentro do template. Lógica: Facilita a referência ao conjunto de produtos no template, permitindo, por exemplo, iterações no loop for.
#7: Configura a paginação para exibir 3 produtos por página. Lógica: Controla a quantidade de produtos mostrados em cada página da lista.

# https://linktr.ee/edsoncopque