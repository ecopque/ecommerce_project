# FILE: /client_profile/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from . import models
from . import forms
from django.contrib.auth.models import User #6:
import copy #7:
from django.contrib.auth import authenticate, login

class BasePerfil(View): #1:
    template_name = 'client_profile/create.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.cart = copy.deepcopy(self.request.session.get('cart', {})) #8:

        self.client_profile = None #9:

        # Checking if you are logged in
        if self.request.user.is_authenticated: #2:
            self.client_profile = models.Client_Profile.objects.filter(user=self.request.user).first() #10:

            self.context = {
                'userform': forms.UserForm(data=self.request.POST or None, user=self.request.user, instance=self.request.user,),
                'perfilform': forms.PerfilForm(data=self.request.POST or None, instance=self.client_profile),
                } #3: ##AAA:
        else:
            self.context = {
                'userform': forms.UserForm(data=self.request.POST or None,),
                'perfilform': forms.PerfilForm(data=self.request.POST or None),
                } #3:
        
        self.userform = self.context['userform'] #11:
        self.perfilform = self.context['perfilform'] #12:
            
        self.new_render = render(self.request, self.template_name, self.context) #4:

    def get(self, *args, **kwargs): #5:
        return self.new_render #5:


class Create(BasePerfil):
    def post(self, *args, **kwargs):
        # if not self.userform.is_valid() or not self.perfilform.is_valid(): #
        if not self.userform.is_valid(): #13:
            print('Invalid')
            return self.new_render

        username = self.userform.cleaned_data.get('username') #14:
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')
        
        # User logged in
        if self.request.user.is_authenticated: #15:
            # user = self.request.user ##
            user = get_object_or_404(User, username=self.request.user.username) #16:

            user.username = username #17:

            if password: #18:
                user.set_password(password) #19:
            
            user.email = email #20:
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            if not self.client_profile: ##
                self.perfilform.cleaned_data['user'] = user ##
                client_profile = models.Client_Profile(**self.perfilform.cleaned_data) ##
                client_profile.save()

        # User not logged in (new) 
        else:
            user = self.userform.save(commit=False) #
            user.set_password(password) #
            user.save() #

            client_profile = self.perfilform.save(commit=False) #21:
            client_profile.user = user #22:
            client_profile.save()
        
        if password: ##
            authentic = authenticate(self.request, username=user, password=password) ##
            if authentic: ##
                login(self.request, user=user) ##

        print('Valid')

        self.request.session['cart'] = self.cart #23:
        self.request.session.save()

        return self.new_render

class Update(View):
    ...

class Login(View):
    ...

class Logout(View):
    ...


#AAA: Adicionamos 'instance=self.client_profile';
# ------------------------------------------------------------------
#6: Importa o modelo User do módulo django.contrib.auth.models. Este modelo é utilizado para representar usuários no sistema, como nas operações de verificação de existência e atualização de dados do usuário.
#7: Importa o módulo copy, que fornece funções para criar cópias superficiais ou profundas de objetos. Neste caso, copy.deepcopy() é utilizado para duplicar o carrinho de compras, garantindo que mudanças na cópia não afetem o objeto original.
#8: Obtém o carrinho de compras da sessão e cria uma cópia profunda para evitar que alterações feitas na cópia afetem o carrinho original armazenado na sessão. Isso é importante para manipular os dados do carrinho de forma segura durante a execução do código.
#9: Inicializa self.client_profile como None, que será utilizado para armazenar o perfil do cliente se ele estiver autenticado. Essa variável é atualizada posteriormente com os dados do perfil, caso o usuário esteja logado.
#10: Busca o perfil do cliente associado ao usuário atualmente autenticado (self.request.user) no banco de dados. Utiliza o módulo models, que faz referência ao arquivo /client_profile/models.py. A função filter() retorna uma lista de resultados, e first() retorna o primeiro item encontrado ou None se nenhum resultado for encontrado.
#11: Atribui a instância do formulário UserForm da chave 'userform' no dicionário de contexto (self.context) à variável self.userform. O formulário é usado para manipular dados do usuário, como nome, senha e e-mail.
#12: Atribui a instância do formulário PerfilForm da chave 'perfilform' no dicionário de contexto (self.context) à variável self.perfilform. Esse formulário é utilizado para lidar com os dados do perfil do cliente.
#13: Verifica se os dados submetidos no formulário UserForm são válidos. A função is_valid() realiza a validação dos dados com base nas regras definidas no formulário, como campos obrigatórios e restrições de formato. Se não forem válidos, o fluxo de execução retorna à renderização da página com os erros.
#14: Extrai o nome de usuário validado (username) do dicionário cleaned_data do formulário UserForm. O dicionário cleaned_data contém os dados validados e processados.
#15: Verifica se o usuário está autenticado. Se estiver, os dados do usuário existente serão atualizados, caso contrário, será criado um novo usuário.
#16: Obtém o objeto User do banco de dados pelo nome de usuário. A função get_object_or_404 retorna o objeto se ele for encontrado ou gera um erro 404 se não for.
#17: Atualiza o nome de usuário do objeto User com o novo valor username.
#18: Verifica se o campo de senha foi preenchido. Se foi, a senha será atualizada.
#19: Atualiza a senha do usuário chamando o método set_password(), que realiza o hash da senha antes de armazená-la no banco de dados.
#20: Atualiza o e-mail do objeto User com o novo valor email.
#21: Salva os dados do formulário PerfilForm em um novo objeto Client_Profile, mas sem gravar no banco de dados ainda. Isso permite associar o perfil ao usuário recém-criado.
#22: Associa o perfil do cliente ao novo usuário criado.
#23: Atualiza o carrinho de compras na sessão com os dados manipulados.
# ------------------------------------------------------------------
#1: Define uma classe de visualização base para lidar com o perfil do cliente.
#2: Verifica se o usuário está autenticado para personalizar o contexto do formulário.
#3: Cria um dicionário de contexto com os formulários UserForm e PerfilForm.
#4: Renderiza a página com o template especificado e o contexto.
#5: Sobrescreve o método get para renderizar a página com o contexto configurado.

# https://linktr.ee/edsoncopque