# FILE: /client_profile/views.py

from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from . import models
from . import forms

class BasePerfil(View): ##
    template_name = 'client_profile/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.context = {
            'userform': forms.UserForm(data=self.request.POST or None),
            'perfilform': forms.PerfilForm(data=self.request.POST or None),
            } ##
        
        self.new_render = render(self.request, self.template_name, self.context) ##

    def get(self, *args, **kwargs): ##
        return self.new_render ##


class Create(BasePerfil):
    ...

class Update(View):
    ...

class Login(View):
    ...

class Logout(View):
    ...


# https://linktr.ee/edsoncopque