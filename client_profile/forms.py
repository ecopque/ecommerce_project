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

    def __init__(self, user=None, *args, **kwargs): #7:
        super().__init__(*args, **kwargs) #8:

        self.user = user #9:

    class Meta:
        model = User #10:
        fields = ('first_name', 'last_name', 'username', 'password', 'password2', 'email') #11:

    def clean(self, *args, **kwargs): #12:
        data = self.data #13:
        cleaned = self.cleaned_data #14:
        validation_error_msgs = {} #15:

        user_data = cleaned.get('username') #16:
        password_data = cleaned.get('password') #17:
        password_data2 = cleaned.get('password2') #17:
        email_data = cleaned.get('email') #18:

        user_db = User.objects.filter(username=user_data).first() #19:
        email_db = User.objects.filter(username=email_data).first() #20:

        error_msg_user_exists = 'User already exists.'
        error_msg_password_match = 'The two passwords do not match.'
        error_msg_email_exists = 'E-mail already exists.'
        error_msg_email_shorts = 'Password must be at least 6 characters long.'

        # Logged in users: update
        if self.user: #21:
            if user_db: #22:
                if user_data != user_db.username: #23:
                    validation_error_msgs['username'] = error_msg_user_exists #24:

            if password_data: #25:
                if password_data != password_data2: #26:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) < 6: #27:
                    validation_error_msgs['password'] = error_msg_email_shorts

            if email_db: #28:
                if email_data != email_db.email: #29:
                    validation_error_msgs['email'] = error_msg_email_exists

        # Users not logged in: registration
        else:
            if user_data != user_db.username:
                validation_error_msgs['username'] = error_msg_user_exists

            if password_data != password_data2:
                validation_error_msgs['password'] = error_msg_password_match
                validation_error_msgs['password2'] = error_msg_password_match

            if len(password_data) < 6:
                validation_error_msgs['password'] = error_msg_email_shorts

            if email_data != email_db.email:
                validation_error_msgs['email'] = error_msg_email_exists

        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))


# ------------------------------------------------------------------
#1: Define um formulário baseado no modelo para o perfil do cliente, utilizando o ModelForm do Django. Essa classe herda funcionalidades de forms.ModelForm, permitindo a criação de formulários com base nos modelos do banco de dados.
#2: Indica que o formulário PerfilForm será baseado no modelo Client_Profile, definido em /client_profile/models.py. Esse modelo especifica os campos e comportamentos que o formulário utilizará para representar os dados do perfil do cliente.
#3: Especifica que todos os campos do modelo Client_Profile serão incluídos no formulário. Isso significa que o formulário terá um campo para cada atributo definido no modelo, exceto os campos explicitamente excluídos.
#4: Exclui o campo user do formulário, ou seja, esse campo não será exibido ou manipulado diretamente no formulário.
#5: Define um formulário para o modelo User, utilizando o ModelForm do Django, permitindo criar e manipular usuários do sistema.
#6: Adiciona campos para senha e confirmação de senha no formulário, com PasswordInput como widget, ocultando os caracteres digitados.
#7: Sobrescreve o método __init__ para aceitar um parâmetro opcional user, além dos argumentos padrões args e kwargs, permitindo personalizar o formulário com base no usuário atual.
#8: Chama o construtor da superclasse (ModelForm) para garantir a inicialização correta dos atributos do formulário.
#9: Armazena o usuário passado como argumento para uso futuro no formulário, por exemplo, para validação personalizada.
#10: Define metadados para o formulário, especificando o modelo User do Django e os campos que serão exibidos e manipulados.
#11: Especifica os campos que serão incluídos no formulário UserForm, permitindo o cadastro ou atualização desses atributos para um usuário.
#12: Sobrescreve o método clean, usado para validação personalizada dos dados do formulário antes de serem salvos.
#13: Obtém os dados enviados no formulário como um dicionário.
#14: Acessa os dados validados e limpos do formulário.
#15: Inicializa um dicionário para armazenar mensagens de erro de validação.
#16: Obtém o nome de usuário inserido no formulário.
#17: Obtém os valores das senhas inseridas no formulário.
#18: Obtém o e-mail inserido no formulário.
#19: Consulta o banco de dados para verificar se já existe um usuário com o nome de usuário fornecido.
#20: Verifica se já existe um usuário com o e-mail fornecido.
#21: Verifica se o usuário está logado. Se estiver, aplica regras específicas para atualização de dados.
#22: Verifica se o nome de usuário já existe no banco de dados.
#23: Verifica se o nome de usuário fornecido é diferente do registrado para o usuário atual.
#24: Adiciona uma mensagem de erro se o nome de usuário já existir.
#25: Verifica se a senha foi fornecida.
#26: Valida se as senhas coincidem, caso contrário, adiciona mensagens de erro.
#27: Verifica se a senha tem pelo menos 6 caracteres. Caso contrário, adiciona uma mensagem de erro.
#28: Verifica se o e-mail já está registrado.
#29: Compara o e-mail fornecido com o registrado no banco de dados.

# https://linktr.ee/edsoncopque