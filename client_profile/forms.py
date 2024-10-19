# FILE: /client_profile/forms.py

from django import forms
from . import models
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm): #1:
    class Meta:
        #IMPORT⬇: /client_profile/models.py
        model = models.Client_Profile #2:
        fields = '__all__' #3:
        exclude = ('user',) #4:

class UserForm(forms.ModelForm): #5:
    password = forms.CharField(required=False, widget=forms.PasswordInput(), label='Password') #6:
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(), label='Password confirmation')


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
            if user_db: ##
                if user_data != user_db.username: ##
                    validation_error_msgs['username'] = error_msg_user_exists ##

            if password_data: ##
                if password_data != password_data2: ##
                    validation_error_msgs['password'] = error_msg_password_match ##
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) < 6: ##
                    validation_error_msgs['password'] = error_msg_email_shorts

            if email_db: ##
                if email_data != email_db.email: ##
                    validation_error_msgs['email'] = error_msg_email_exists

        # Users not logged in: registration
        else:
            validation_error_msgs['username'] = 'XXX'

        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))


#1: Define um formulário baseado no modelo para o perfil do cliente, utilizando o ModelForm do Django. Essa classe herda funcionalidades de forms.ModelForm, permitindo a criação de formulários com base nos modelos do banco de dados.
#2: Indica que o formulário PerfilForm será baseado no modelo Client_Profile, definido em /client_profile/models.py. Esse modelo especifica os campos e comportamentos que o formulário utilizará para representar os dados do perfil do cliente.
#3: Especifica que todos os campos do modelo Client_Profile serão incluídos no formulário. Isso significa que o formulário terá um campo para cada atributo definido no modelo, exceto os campos explicitamente excluídos.
#4: Exclui o campo user do formulário, ou seja, esse campo não será exibido ou manipulado diretamente no formulário.
#5: Define um formulário para o modelo User, utilizando o ModelForm do Django, permitindo criar e manipular usuários do sistema.
#6: Adiciona campos para senha e confirmação de senha no formulário, com PasswordInput como widget, ocultando os caracteres digitados.
#7: 

# https://linktr.ee/edsoncopque