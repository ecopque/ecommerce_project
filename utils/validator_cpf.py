# FILE: /utils/validator_cpf.py

import re

def validator_cpf(cpf):
   cpf_user = str(cpf)
   cpf_user = re.sub(r'[^0-9]', '', cpf_user) #1:

   if not cpf_user or len(cpf_user) != 11: #2:
      return False
   
   new_cpf = cpf_user[:-2] #3:
   reverse = 10
   total = 0

   for index in range(19):
      if index > 8: #4:
         index -= 9 #4:
      
      total += int(new_cpf[index]) * reverse #5:

      reverse -= 1 #6:
      if reverse < 2: #7:
         reverse = 11
         d = 11 - (total % 11) #8:

         if d > 9: #9:
            d = 0
            total = 0
            new_cpf += str(d) #10:

   sequence = new_cpf == str(new_cpf[0]) * len(cpf_user) #11:
   if cpf_user == new_cpf and not sequence:
      return True
   else:
      return False
   

# ------------------------------------------------------------------
#1: Esta linha utiliza a função sub do módulo re (expressões regulares) para remover todos os caracteres não numéricos do cpf_user. Assim, se o usuário inserir caracteres como pontos ou traços, eles serão eliminados. O resultado é que cpf_user conterá apenas números, o que é essencial para a validação do CPF.
#2: Aqui, a função verifica se cpf_user está vazio ou se não contém exatamente 11 dígitos. Se qualquer uma dessas condições for verdadeira, a função retorna False, indicando que o CPF não é válido. Essa verificação é importante para garantir que o CPF tenha o formato esperado antes de realizar validações adicionais.
#3: Esta linha cria uma nova string new_cpf que contém todos os caracteres de cpf_user, exceto os últimos dois. Esses últimos dois dígitos são usados para validar o CPF, portanto, eles não são incluídos nessa parte do código. Essa operação é importante porque a validação do CPF se baseia nos primeiros nove dígitos.
#4: O loop for itera 19 vezes para calcular os dois dígitos de verificação do CPF. A linha if index > 8: altera o valor de index para garantir que a lógica de cálculo dos dígitos de verificação utilize os primeiros nove dígitos (de 0 a 8) do CPF durante as primeiras iterações e, em seguida, repete os cálculos com os nove primeiros dígitos para calcular o segundo dígito de verificação. Isso é feito para lidar com a forma como o CPF é validado.
#5: Esta linha acumula o valor em total somando o produto do dígito na posição index de new_cpf (convertido para inteiro) e o valor atual de reverse. O valor de reverse começa em 10 e diminui a cada iteração do loop. Essa linha é fundamental, pois está realizando o cálculo necessário para determinar o primeiro dígito verificador.
#6: Após cada iteração do loop, reverse é decrementado em 1. A variável reverse é usada como um fator multiplicador para calcular o total necessário para determinar os dígitos de verificação do CPF. Este decremento é parte da lógica de validação, pois os fatores começam em 10 e vão até 2.
#7: Quando reverse é menor que 2, significa que o primeiro dígito de verificação foi calculado e agora o código está se preparando para calcular o segundo dígito. Essa condição é necessária para reiniciar o cálculo com um novo valor de reverse e totalizar os dígitos adequadamente.
#8: Se reverse for menor que 2, esta linha redefine o valor de reverse para 11. Isso é necessário para iniciar o cálculo do segundo dígito verificador do CPF, que tem um peso diferente em relação ao primeiro.
#9: Esta condição verifica se o valor de d é maior que 9. Como os dígitos verificadores do CPF não podem ser superiores a 9, esta condição é importante para assegurar que d esteja dentro do intervalo válido.
#10: Esta linha adiciona o dígito verificador calculado (d) ao final de new_cpf, formando assim o CPF completo com os dois dígitos verificadores.
#11: Aqui, sequence verifica se todos os dígitos de new_cpf são iguais ao primeiro dígito. Isso é uma verificação adicional para evitar CPFs que consistem apenas em dígitos repetidos (como "111.111.111-11"), que são considerados inválidos.

# https://linktr.ee/edsoncopque