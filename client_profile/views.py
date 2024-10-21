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
        
        self.userform = self.context['userform'] ##
        self.perfilform = self.context['perfilform'] ##
            
        self.new_render = render(self.request, self.template_name, self.context) #4:

    def get(self, *args, **kwargs): #5:
        return self.new_render #5:


class Create(BasePerfil):
    def post(self, *args, **kwargs):
        # if not self.userform.is_valid() or not self.perfilform.is_valid():
        if not self.userform.is_valid(): ##
            print('Invalid')
            return self.new_render

        username = self.userform.cleaned_data.get('username') ##
        password = self.userform.cleaned_data.get('password') ##
        email = self.userform.cleaned_data.get('email') ##
        first_name = self.userform.cleaned_data.get('first_name') ##
        last_name = self.userform.cleaned_data.get('last_name') ##
        
        # User logged in
        if self.request.user.is_authenticated: ##
            user = self.request.user ##
            user.username = username ##

            if password: ##
                user.set_password(password) ##
            
            user.email = email ##
            user.first_name = first_name ##
            user.last_name = last_name ##
            user.save() ##

        # User not logged in (new) 
        else:
            user = self.userform.save(commit=False) ##
            user.set_password(password) ##
            user.save() ##

            client_profile = self.perfilform.save(commit=False) ##
            client_profile.user = user ##
            client_profile.save() ##

        print('Valid')
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