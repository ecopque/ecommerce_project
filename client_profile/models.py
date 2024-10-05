# FILE: /client_profile/models.py

from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re
from utils.validator_cpf import validator_cpf

#URL⬇: http://127.0.0.1:8000/admin/client_profile/client_profile/add/
class Client_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    date_birth = models.DateField()
    cpf = models.CharField(max_length=11, verbose_name='CPF', default='0000000000')
    
    # Padrão Correios:
    address = models.CharField(max_length=50)
    number = models.CharField(max_length=5)
    complement = models.CharField(max_length=30)
    
    neighborhood = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    city = models.CharField(max_length=30)
    state = models.CharField(
        max_length=2,
        default='SP',
        choices = (
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
            )
    ) #1:

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def clean(self): #2:
        error_messages = {} #2:
        
        # Refazer essa validação no 'validator_cpf.py':
        # if not validator_cpf(self.cpf): ##
        #     error_messages['cpf'] = 'Enter a valid CPF.'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8: #3:
            error_messages['cep'] = 'Enter a valid CEP.'

        if error_messages: #4:
            raise ValidationError(error_messages) #4:

    class Meta:
        verbose_name = 'Client Profile'
        verbose_name_plural = 'Client Profiles'


#1: Quando você usa o Django Admin para adicionar ou editar instâncias do seu modelo, você verá os valores legíveis (neste caso, "Acre" e "Alagoas"). Isso é fornecido pela tupla que você definiu, onde o primeiro elemento (ex: 'AC') é o valor que será armazenado no banco de dados e o segundo elemento (ex: 'Acre') é o texto que será exibido na interface. O Django armazenará o valor da primeira parte da tupla (ou seja, 'AC' para Acre e 'AL' para Alagoas) no banco de dados. Portanto, na tabela correspondente ao modelo Client_Profile, você verá os códigos de estado ('AC', 'AL', etc.) armazenados no campo state.
#2: O método clean é chamado automaticamente pelo Django quando o objeto está sendo validado. Serve para realizar validações personalizadas, além das já feitas pelos campos padrão. Indica o início do método e a criação do dicionário error_messages, que armazenará quaisquer mensagens de erro relacionadas à validação do CPF, CEP ou outros campos.
#3: Aqui, o código valida o campo cep. O padrão re.search(r'[^0-9]', self.cep) verifica se há algum caractere que não seja um número no CEP, enquanto len(self.cep) < 8 assegura que o CEP tenha o comprimento correto (8 dígitos). Se qualquer uma dessas condições for verdadeira, uma mensagem de erro é adicionada a error_messages. O ## marca a finalização da expressão de validação.
#4: Se o dicionário error_messages contiver algum erro (ou seja, se algum campo falhar na validação), o Django levantará uma exceção ValidationError, que exibirá as mensagens de erro associadas. Essas linhas marcam o encerramento da lógica de validação no método clean.

# https://linktr.ee/edsoncopque