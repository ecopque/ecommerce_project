# FILE: /product/templatetags/brfilters.py

from django.template import Library
from utils import utils

register = Library() #1:

@register.filter #2:
def format_price(value): #3:
    return utils.format_pricevrs(value) #3:

@register.filter
def cart_total(cart): #4:
    return utils.cart_total_qtd(cart) #4:

@register.filter
def cart_totals(cart): #5:
    return utils.cart_totals_products(cart) #5:


#5: A função cart_totals é um filtro de template do Django, que usa a função cart_totals_products do módulo utils para calcular o total dos preços dos produtos no carrinho. @register.filter: Isso registra a função como um filtro de template, permitindo que seja usada diretamente nos templates do Django.
# ------------------------------------------------------------------
#4: Define um filtro personalizado (cart_total) que usa a função cart_total_qtd para calcular o total de itens no carrinho, sendo utilizado em templates para exibir essa informação.
# ------------------------------------------------------------------
#1: Cria uma instância de Library para registrar filtros personalizados. Lógica: Essa linha é necessária para permitir que você adicione filtros personalizados no sistema de templates do Django.
#2: Um decorador que registra a função format_price como um filtro de template. Lógica: O decorador permite que a função seja usada nos templates do Django como um filtro aplicado em variáveis, por exemplo, {{ price|format_price }}.
#3: Chama a função format_pricevrs no módulo utils para formatar o valor. Lógica: A separação da lógica de formatação para o arquivo utils.py mantém o código modular e reutilizável.

# https://linktr.ee/edsoncopque