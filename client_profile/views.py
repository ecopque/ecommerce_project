#FILE: /client_profile/views.py

from django.shortcuts import render
from django.views.generic import ListView
from django.views import View


class BasePerfil(View): ##
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.new_render = render() ##

class Create(BasePerfil):
    ...

class Update(View):
    ...

class Login(View):
    ...

class Logout(View):
    ...


# https://linktr.ee/edsoncopque