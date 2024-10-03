from django.contrib import admin
from order.models import Order, OrderItem

class OrderItemInline(admin.TabularInline): #1:
    model = OrderItem #2:
    extra = 3

class OrderAdmin(admin.ModelAdmin): #3:
    inlines = [OrderItemInline] #4:

admin.site.register(Order, OrderAdmin) #5:
admin.site.register(OrderItem) #6:


# ------------------------------------------------------------------
#1: Esta classe define um TabularInline, que permite a edição de múltiplos objetos OrderItem diretamente na página de administração de um Order. Isso cria uma interface mais prática para gerenciar itens de pedidos no Django Admin.
#2: Especifica que o modelo que será gerido por este TabularInline é o OrderItem. Ele vincula o comportamento do inline ao modelo correto.
#3: Esta classe personaliza a administração do modelo Order no Django Admin. Através da adição de inlines, ela possibilita a edição de itens do pedido na mesma página de administração do pedido.
#4: Adiciona o OrderItemInline à interface de administração de Order. Isso permite que os itens do pedido sejam gerenciados junto com o pedido na mesma página.
#5: Registra o modelo Order junto com a configuração personalizada OrderAdmin no Django Admin, permitindo a administração do modelo de forma customizada.
#6: Registra o modelo OrderItem no Django Admin, permitindo que os itens de pedido sejam gerenciados diretamente na interface de administração.

# https://linktr.ee/edsoncopque