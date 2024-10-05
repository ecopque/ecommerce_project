# FILE: /utils/validator_cpf.py

import re

def validator_cpf(cpf):
   cpf_user = str(cpf)
   cpf_user = re.sub(r'[^0-9]', '')

   if not cpf or len(cpf_user) != 11: ##
      return False
   
   new_cpf = cpf_user[:-2] #1: ##
   reverse = 10 #2:
   total = 0

   for index in range(19):
      if index > 8: #3:
         index -= 9 #4: ##
      total += int(new_cpf[index]) * reverse #5: ##

      reverse -= 1 ##
      if reverse < 2:
         reverse = 11
         d = 11 - (total % 11) ##

         if d > 9:
            d = 0
            total = 0
            new_cpf += str(d) ##

   sequence = new_cpf == str(new_cpf[0]) * len(cpf_user) ##
   if cpf_user == new_cpf and not sequence: ##
      return True
   else:
      return False



#1: Elimina os dois últimos dígitos do CPF;
#2: Contador reverso;
#3: Primeiro índice vai de 0 a 9;
#4: São os primeiros 9 dígitos do cpf;

# ------------------------------------------------------------------
# # URL: https://github.com/ecopque/cpf_validator
# entrada = input('Digite um CPF: ')
# cpf_usuario = re.sub(r'[^0-9]', '', entrada) # peneira

# repeticao = entrada == entrada[0] * len(entrada)
# if repeticao is True:
#    print('Você repetiu alguns caracteres.')
#    sys.exit()

# nove_digitos = cpf_usuario[:9]
# contagem_regressiva = 10
# hd_soma = 0
# for numero in nove_digitos:
#    hd_soma += int(numero) * contagem_regressiva
#    contagem_regressiva -= 1
# resto_div = (hd_soma * 10) % 11
# resultado = resto_div if resto_div <= 9 else 0

# dez_digitos = nove_digitos + str(resultado)
# contagem_regressiva2 = 11
# hd_soma2 = 0
# for numero2 in dez_digitos:
#    hd_soma2 += int(numero2) * contagem_regressiva2
#    contagem_regressiva2 -= 1
# resto_div2 = (hd_soma2 * 10) % 11
# resultado2 = resto_div2 if resto_div2 <= 9 else 0

# novo_cpf = f'{nove_digitos}{resultado}{resultado2}'
# print(f'Primeiro dígito: {resultado}. Segundo dígito: {resultado2}.')
# if cpf_usuario == novo_cpf:
#    print(f'CPF: {cpf_usuario} é válido.')
# else:
#    print(f'CPF: {cpf_usuario} é inválido.')

# https://linktr.ee/edsoncopque