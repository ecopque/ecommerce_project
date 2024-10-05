# FILE: /client_profile/models.py

from django.db import models
from django.contrib.auth.models import User

class Client_Profile(models.Model): ##
    user = models.OneToOneField(User, on_delete=models.CASCATE) ##
    age = models.PositiveIntegerField() ##
    date_birth = models.DateField() ##
    cpf = models.CharField(max_length=11) ##
    
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
    
    def clean(self):
        pass

    class Meta:
        verbose_name = 'Client Profile'
        verbose_name_plural = 'Client Profiles'



# https://linktr.ee/edsoncopque