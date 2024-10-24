# FILE: /order/views.py

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib import messages
from product.models import Variation

class Pay(View):
    # IMPORT⬇: /order/templates/order/pay.html
    template_name = 'order/pay.html' ##

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated: #1: ##
            messages.error(self.request, 'You need to log in.')
            return redirect('client_profile:create')
        
        if not self.request.session.get('cart'): #2: ##
            messages.error(self.request, 'Empty cart.')
            return redirect('product:list')
        
        cart = self.request.session.get('cart') #3: ##
        # cart_variation_ids = [v for v in cart]
        # print(cart_variation_ids)
        
        cart_variation_ids = []
        for v in cart: ##
            cart_variation_ids.append(v)
        print(cart_variation_ids)

        # IMPORT⬇: /product/models.py
        bd_variations = list(Variation.objects.select_related('product').filter(id__in=cart_variation_ids)) #4: ##
        
        for variation in bd_variations: ##
            vid = str(variation.id) ##
            
            # IMPORT⬇: /product/models.py
            stock = variation.stock ##

            # IMPORT⬇: /product/views.py
            qtd_cart = cart[vid]['quantitative'] ##
            price_unt = cart[vid]['unit_price'] ##
            price_unt_promo = cart[vid]['promotional_unit_price'] ##
            
            error_msg_stock = ''

            if stock < qtd_cart:
                # IMPORT⬇: /product/views.py
                cart[vid]['quantitative'] = stock ##
                cart[vid]['quantitative_price'] = stock * price_unt ##
                cart[vid]['promotional_quantitative_price'] = stock * price_unt_promo ##
                
                error_msg_stock = 'Insufficient stock for some products in your cart. We have reduced the quantity of some products.'
            
            if error_msg_stock: ##
                messages.error(self.request, error_msg_stock)

                self.request.session.save()
                return redirect('product:cart') ##

        context = {}
        return render(self.request, self.template_name, context) ##

class SaveOrder(View):
    ...

class Details(View):
    ...


#1: Se não estiver logado e tentar acessar '127.0.0.1:8000/order/', será redirecionado para a página de 'create' e receberá uma mensagem de erro. ;
#2: Mesmo se estiver logado e tentar acessar '127.0.0.1:8000/order/' e não houver itens no carrinho, será redirecionado para 'list' e receberá mensagem de erro;
#3: Aqui estamos obtendo as chaves, em nosso caso as 'IDs' para trabalhar a questão se tem estoque quando cliente for emitir o pedido;
#4: Aqui estamos tendo acesso [selecionando] às variações. Este 'select_related' foi para diminuir outras consultas que estavam aparecendo no relatório do Django;


# https://linktr.ee/edsoncopque