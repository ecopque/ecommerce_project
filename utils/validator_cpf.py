# FILE: /utils/validator_cpf.py

import re

def validator_cpf(cpf):
   cpf_user = str(cpf)
   cpf_user = re.sub(r'[^0-9]', '', cpf_user) ##

   if not cpf_user or len(cpf_user) != 11: ##
      return False
   
   new_cpf = cpf_user[:-2] ##
   reverse = 10 ##
   total = 0 ##

   for index in range(19):
      if index > 8: ##
         index -= 9 ##
      
      total += int(new_cpf[index]) * reverse ##

      reverse -= 1 ##
      if reverse < 2: ##
         reverse = 11 ##
         d = 11 - (total % 11) ##

         if d > 9: ##
            d = 0 ##
            total = 0 ##
            new_cpf += str(d) ##

   sequence = new_cpf == str(new_cpf[0]) * len(cpf_user) ##
   if cpf_user == new_cpf and not sequence: ##
      return True
   else:
      return False


# https://linktr.ee/edsoncopque