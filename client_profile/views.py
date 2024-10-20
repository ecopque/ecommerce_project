# FILE: /client_profile/views.py

from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from . import models
from . import forms

class BasePerfil(View): #1:
    template_name = 'client_profile/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.client_profile = None ##

        # Checking if you are logged in
        if self.request.user.is_authenticated: #2:
            self.client_profile = models.Client_Profile.objects.filter(user=self.request.user).first() ##

            self.context = {
                'userform': forms.UserForm(data=self.request.POST or None, user=self.request.user, instance=self.request.user,),
                'perfilform': forms.PerfilForm(data=self.request.POST or None),
                } #3:
        else:
            self.context = {
                'userform': forms.UserForm(data=self.request.POST or None,),
                'perfilform': forms.PerfilForm(data=self.request.POST or None),
                } #3:
            
        self.new_render = render(self.request, self.template_name, self.context) #4:

    def get(self, *args, **kwargs): #5:
        return self.new_render #5:


class Create(BasePerfil):
    def post(self, *args, **kwargs):
        print(self.client_profile)
        return self.new_render

class Update(View):
    ...

class Login(View):
    ...

class Logout(View):
    ...


# ------------------------------------------------------------------
#1: Define uma classe de visualização base para lidar com o perfil do cliente.
#2: Verifica se o usuário está autenticado para personalizar o contexto do formulário.
#3: Cria um dicionário de contexto com os formulários UserForm e PerfilForm.
#4: Renderiza a página com o template especificado e o contexto.
#5: Sobrescreve o método get para renderizar a página com o contexto configurado.

# https://linktr.ee/edsoncopque