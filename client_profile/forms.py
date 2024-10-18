# FILE: /client_profile/forms.py

from django import forms
from . import models
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm): ##
    class Meta:
        #IMPORT⬇: /client_profile/models.py
        model = models.Client_Profile ##
        fields = '__all__' ##
        exclude = ('user',) ##

class UserForm(forms.ModelForm): ##
    class Meta:
        model = User ##
        fields = ('first_name', 'last_name', 'username', 'password', 'email') ##

    def clean(self, *args, **kwargs): ##
        data = self.data ##
        cleaned = self.cleaned_data ##



# https://linktr.ee/edsoncopque