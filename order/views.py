# FILE: /order/views.py

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views import View
from django.contrib import messages

class Pay(ListView):
    # IMPORT⬇: /order/templates/order/pay.html
    template_name = 'order/pay.html' ##

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated: ##
            messages.error(self.request, 'You need to log in.')
            return redirect('client_profile:create')

        context = {}
        return render(self.request, self.template_name, context) ##

class SaveOrder(View):
    ...

class Details(View):
    ...


# https://linktr.ee/edsoncopque