# FILE: /order/views.py

from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages
from product.models import Variation
from utils import utils
from .models import Order, OrderItem
from django.http import HttpResponse

class DispatchLoginRequired(View):
    def dispatch(self, *args, **kwargs): ##
        if not self.request.user.is_authenticated: ##
            return redirect('client_profile:create')
        return super().dispatch(*args, **kwargs) ##

class Pay(DispatchLoginRequired, DetailView): ##
    template_name = 'order/pay.html'
    
    # IMPORT⬇: /order/models.py
    model = Order
    pk_url_kwarg = 'pk' ##
    context_object_name = 'order'
    

class SaveOrder(View):
    # IMPORT⬇: /order/templates/order/pay.html
    template_name = 'order/pay.html' #5:

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated: #1: #6:
            messages.error(self.request, 'You need to log in.')
            return redirect('client_profile:create')
        
        if not self.request.session.get('cart'): #2: #7:
            messages.error(self.request, 'Empty cart.')
            return redirect('product:list')
        
        cart = self.request.session.get('cart') #3: #8:
        # cart_variation_ids = [v for v in cart]
        # print(cart_variation_ids)
        
        cart_variation_ids = []
        for v in cart: #9:
            cart_variation_ids.append(v)
        print(cart_variation_ids)

        # IMPORT⬇: /product/models.py
        bd_variations = list(Variation.objects.select_related('product').filter(id__in=cart_variation_ids)) #4: #10:
        
        for variation in bd_variations: #11:
            vid = str(variation.id) #12:
            
            # IMPORT⬇: /product/models.py
            stock = variation.stock #13:

            # IMPORT⬇: /product/views.py
            qtd_cart = cart[vid]['quantitative'] #14:
            price_unt = cart[vid]['unit_price'] #15:
            price_unt_promo = cart[vid]['promotional_unit_price'] #16:
            
            error_msg_stock = ''

            if stock < qtd_cart:
                # IMPORT⬇: /product/views.py
                cart[vid]['quantitative'] = stock #17:
                cart[vid]['quantitative_price'] = stock * price_unt #18:
                cart[vid]['promotional_quantitative_price'] = stock * price_unt_promo #19:
                
                error_msg_stock = 'Insufficient stock for some products in your cart. We have reduced the quantity of some products.'
            
            if error_msg_stock:
                messages.error(self.request, error_msg_stock)

                self.request.session.save()
                return redirect('product:cart') #20:
        
        # IMPORT⬇: /utils/utils.py
        total_qtd_cart = utils.cart_total_qtd(cart) #21:
        total_value_cart = utils.cart_totals_products(cart) #22:
        
        # IMPORT⬇: /order/models.py
        order = Order(user=self.request.user, total=total_value_cart, total_qtd=total_qtd_cart, status='C') #23:
        order.save()

        OrderItem.objects.bulk_create(
            [
                OrderItem(
                    #IMPORT⬇: /order/models.py
                    order=order, #24:
                    product_name=v['product_name'], #25:
                    product_id=v['product_id'],
                    variation=v['variation_name'],
                    variation_id=v['variation_id'],

                    # IMPORT⬇: /order/models.py | /order/views.py
                    price=v['quantitative_price'], #26:
                    price_promotional=v['promotional_quantitative_price'], #27:

                    # IMPORT⬇: /order/views.py | /order/models.py
                    quantitative=v['quantitative'],
                   
                    #IMPORT⬇: /order/models.py
                    image=v['image'], #28:
                )
                for v in cart.values()
            ]
        )

        del self.request.session['cart'] #29:
        # return redirect('order:list')

        # order = /order/views.py
        return redirect(reverse('order:pay', kwargs={'pk': order.pk})) ##


class Details(View):
    ...

class List(View):
    def get(self, *args, **kwargs):
        return HttpResponse('List')


# ------------------------------------------------------------------
#5: Essa linha define o caminho do template HTML (order/pay.html) que será utilizado para renderizar a página de pagamento. É necessário para que a view Pay saiba qual arquivo de template exibir quando a requisição for feita.
#6: Verifica se o usuário não está autenticado. Caso o usuário não esteja logado, uma mensagem de erro é enviada e o usuário é redirecionado para a página de criação de perfil (client_profile:create). Isso assegura que apenas usuários autenticados possam acessar essa view.
#7: Verifica se o carrinho de compras não existe na sessão. Se o carrinho estiver vazio ou não estiver presente, uma mensagem de erro é exibida e o usuário é redirecionado para a lista de produtos (product:list). Isso garante que a operação de pagamento só seja possível se o usuário tiver itens no carrinho.
#8: Recupera o carrinho de compras armazenado na sessão do usuário. O carrinho é um dicionário que contém informações sobre os produtos que o usuário pretende comprar, como quantidade, preço, etc.
#9: Itera sobre os itens do carrinho. A variável v representa a chave de cada item no dicionário cart. Durante o loop, os IDs das variações dos produtos são coletados para serem usados em consultas ao banco de dados.
#10: Realiza uma consulta no banco de dados para obter as variações dos produtos que estão no carrinho, utilizando os IDs coletados. O método select_related('product') é usado para otimizar o carregamento do objeto relacionado product, evitando consultas adicionais ao banco.
#11: Itera sobre as variações de produtos obtidas do banco de dados. Cada variation representa uma variação específica de um produto.
#12: Converte o ID da variação (variation.id) para uma string e o armazena na variável vid. Esse ID é usado para acessar informações específicas do produto no dicionário cart.
#13: Obtém a quantidade em estoque da variação do produto atual. Isso é usado para verificar se há estoque suficiente para atender ao pedido.
#14: Recupera a quantidade solicitada do produto no carrinho. cart[vid] acessa as informações do produto correspondente no dicionário do carrinho.
#15: Obtém o preço unitário do produto no carrinho.
#16: Obtém o preço promocional unitário do produto no carrinho, se existir.
#17: Atualiza a quantidade do produto no carrinho para o valor do estoque disponível, caso o estoque seja inferior à quantidade solicitada originalmente.
#18: Recalcula o preço total do produto no carrinho com base na quantidade disponível em estoque e no preço unitário.
#19: Recalcula o preço total promocional do produto com base na quantidade disponível em estoque e no preço unitário promocional.
#20: Redireciona o usuário para a página do carrinho (product:cart) caso haja problemas com o estoque, para que ele possa revisar os itens.
#21: Chama a função cart_total_qtd do módulo utils para calcular o total de itens no carrinho.
#22: Chama a função cart_totals_products do módulo utils para calcular o valor total dos produtos no carrinho.
#23: Cria uma instância de Order com os dados do usuário, o valor total do carrinho, a quantidade total de itens e o status C (Created).
#24: Referencia o pedido recém-criado na criação de cada item do pedido (OrderItem). Isso cria a associação entre os itens e o pedido.
#25: Define o nome do produto no item do pedido.
#26: Define o preço total do produto, baseado na quantidade, no item do pedido.
#27: Define o preço promocional total do produto, baseado na quantidade, no item do pedido.
#28: Define a imagem do produto no item do pedido.
#29: Remove o carrinho da sessão após a conclusão do pedido, limpando os itens para o próximo uso.
# ------------------------------------------------------------------
#1: Se não estiver logado e tentar acessar '127.0.0.1:8000/order/', será redirecionado para a página de 'create' e receberá uma mensagem de erro. ;
#2: Mesmo se estiver logado e tentar acessar '127.0.0.1:8000/order/' e não houver itens no carrinho, será redirecionado para 'list' e receberá mensagem de erro;
#3: Aqui estamos obtendo as chaves, em nosso caso as 'IDs' para trabalhar a questão se tem estoque quando cliente for emitir o pedido;
#4: Aqui estamos tendo acesso [selecionando] às variações. Este 'select_related' foi para diminuir outras consultas que estavam aparecendo no relatório do Django;


# https://linktr.ee/edsoncopque