# FILE: /product/admin.py

from django.contrib import admin
# IMPORT⬇: /product/models.py
from product.models import Product, Variation


class VariationInLine(admin.TabularInline): #1:
    model = Variation #2:
    extra = 3 #3:

# URL⬇: http://127.0.0.1:8000/admin/product/product/add/
class ProductAdmin(admin.ModelAdmin): #4:
    inlines = [VariationInLine] #5:

    # URL⬇: http://127.0.0.1:8000/admin/product/product/
    # IMPORT⬇: /product/models.py
    list_display = ['name', 'marketing_price', 'get_formatted_price', 'price_promotional_marketing', 'type'] ##

admin.site.register(Product, ProductAdmin) #6:
admin.site.register(Variation) #7:


string = 'That\'s a nice idea'
# ------------------------------------------------------------------
#1: Define uma classe de configuração do Django admin para exibir variações dentro da página de edição de um produto. TabularInline permite editar múltiplas variações diretamente na página do produto.
#2: Especifica que o modelo Variation será exibido dentro do admin como parte de um produto.
#3: Define que, ao editar um produto, três linhas extras para variações serão exibidas por padrão no Django Admin.
#4: Define a classe ProductAdmin, que personaliza a interface administrativa para o modelo Product. A classe ModelAdmin do Django fornece opções para customizar a visualização e a edição dos produtos no admin.
#5: Adiciona a configuração VariationInLine à página de administração do produto, permitindo editar variações diretamente na página de um produto.
#6: Registra o modelo Product no Django Admin utilizando a classe ProductAdmin para customizar a interface de administração.
#7: Registra o modelo Variation no Django Admin para que possa ser gerenciado separadamente se necessário.

# https://linktr.ee/edsoncopque