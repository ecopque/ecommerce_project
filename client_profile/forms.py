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
    
    password = forms.CharField(required=False, widget=forms.PasswordInput(), label='Password') ##
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(), label='Password confirmation') ##


    def __init__(self, user=None, *args, **kwargs): ##
        super().__init__(*args, **kwargs) ##

        self.user = user ##

    class Meta:
        model = User ##
        fields = ('first_name', 'last_name', 'username', 'password', 'password2', 'email') ##

    def clean(self, *args, **kwargs): ##
        data = self.data ##
        cleaned = self.cleaned_data ##
        validation_error_msgs = {} ##

        if self.user: ##
            print('Logged in')
        
        else:
            ...



# https://linktr.ee/edsoncopque