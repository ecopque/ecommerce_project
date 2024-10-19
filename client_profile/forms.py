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

        user_data = cleaned.get('username') ##
        password_data = cleaned.get('password') ##
        password_data2 = cleaned.get('password2') ##
        email_data = cleaned.get('email') ##

        user_db = User.objects.filter(username=user_data).first() ##
        email_db = User.objects.filter(username=email_data).first() ##

        error_msg_user_exists = 'User already exists.'
        error_msg_password_match = 'The two passwords do not match.'
        error_msg_email_exists = 'E-mail already exists.'
        error_msg_email_shorts = 'Password must be at least 6 characters long.'

        # Logged in users: update
        if self.user: ##
            if user_data != user_db: ##
                if user_db: ##
                    validation_error_msgs['username'] = error_msg_user_exists ##

            if password_data: ##
                if password_data != password_data2: ##
                    validation_error_msgs['password'] = error_msg_password_match ##
                    validation_error_msgs['password2'] = error_msg_password_match
        
        # Users not logged in: registration
        else:
            ...



# https://linktr.ee/edsoncopque