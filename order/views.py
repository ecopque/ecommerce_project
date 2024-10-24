# FILE: /order/views.py

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib import messages

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
        # cart_variation_id = [v for v in cart]
        # print(cart_variation_id)
        
        cart_variation_id = []
        for v in cart: ##
            cart_variation_id.append(v)
        print(cart_variation_id)

        context = {}
        return render(self.request, self.template_name, context) ##

class SaveOrder(View):
    ...

class Details(View):
    ...

#1: Se não estiver logado e tentar acessar '127.0.0.1:8000/order/', será redirecionado para a página de 'create' e receberá uma mensagem de erro. ;
#2: Mesmo se estiver logado e tentar acessar '127.0.0.1:8000/order/' e não houver itens no carrinho, será redirecionado para 'list' e receberá mensagem de erro;
#3: Aqui estamos obtendo as chaves, em nosso caso as 'IDs';


# https://linktr.ee/edsoncopque