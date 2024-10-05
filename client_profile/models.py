# FILE: /client_profile/models.py

from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
import re
from utils.validator_cpf import validator_cpf

#URL⬇: http://127.0.0.1:8000/admin/client_profile/client_profile/add/
class Client_Profile(models.Model): ##
    user = models.OneToOneField(User, on_delete=models.CASCADE) ##
    age = models.PositiveIntegerField() ##
    date_birth = models.DateField() ##
    cpf = models.CharField(max_length=11, verbose_name='CPF', default='0000000000') ##
    
    # Padrão Correios:
    address = models.CharField(max_length=50) ## 
    number = models.CharField(max_length=5) ##
    complement = models.CharField(max_length=30) ##
    
    neighborhood = models.CharField(max_length=30) ##
    cep = models.CharField(max_length=8) ##
    city = models.CharField(max_length=30) ##
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
    ) ##

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def clean(self): ##
        error_messages = {} ##
        
        # error
        # if not validator_cpf(self.cpf): ##
        #     error_messages['cpf'] = 'Enter a valid CPF.'

        if re.search(r'[^0-9]', self.cep) or len(self.cep) < 8: ##
            error_messages['cep'] = 'Enter a valid CEP.'

        if error_messages: ##
            raise ValidationError(error_messages) ##

    class Meta:
        verbose_name = 'Client Profile'
        verbose_name_plural = 'Client Profiles'


# https://linktr.ee/edsoncopque