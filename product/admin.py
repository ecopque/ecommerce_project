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
    list_display = ['name', 'marketing_price', 'get_formatted_price', 'price_promotional_marketing', 'type'] #8:

admin.site.register(Product, ProductAdmin) #6:
admin.site.register(Variation) #7:


# ------------------------------------------------------------------
#8: No Django Admin, o atributo list_display define quais campos e métodos da classe Product serão exibidos na lista de produtos. Aqui, os campos name, marketing_price, price_promotional_marketing, e type são exibidos, junto com o método get_formatted_price. get_formatted_price está sendo solicitado diretamente no painel administrativo do Django para exibir o preço formatado.
# ------------------------------------------------------------------
#1: Define uma classe de configuração do Django admin para exibir variações dentro da página de edição de um produto. TabularInline permite editar múltiplas variações diretamente na página do produto.
#2: Especifica que o modelo Variation será exibido dentro do admin como parte de um produto.
#3: Define que, ao editar um produto, três linhas extras para variações serão exibidas por padrão no Django Admin.
#4: Define a classe ProductAdmin, que personaliza a interface administrativa para o modelo Product. A classe ModelAdmin do Django fornece opções para customizar a visualização e a edição dos produtos no admin.
#5: Adiciona a configuração VariationInLine à página de administração do produto, permitindo editar variações diretamente na página de um produto.
#6: Registra o modelo Product no Django Admin utilizando a classe ProductAdmin para customizar a interface de administração.
#7: Registra o modelo Variation no Django Admin para que possa ser gerenciado separadamente se necessário.

# https://linktr.ee/edsoncopque