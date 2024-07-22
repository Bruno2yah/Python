import os
import random

os.system('cls')

cpf_nove_digitos = ''
# random.randint(inicial, fim)
for i in range(9):
    cpf_nove_digitos += str(random.randint(0,9))

soma = 0
i = 10
# soma
for digito in cpf_nove_digitos:
    multiplicacao = int(digito) * i
    soma += multiplicacao
    i -= 1

resultado = (soma*10)%11
primeiro_digito = resultado  if resultado <=9 else 0

cpf_dez_digitos = cpf_nove_digitos + str(primeiro_digito)

soma = 0
i = 11
for digito in cpf_dez_digitos:
    multiplicacao = int(digito)*i
    soma += multiplicacao
    i -= 1

resultado = (soma*10) % 11
segundo_digito = resultado if resultado <= 9 else 0
cpf_gerado_pelo_calculo = f'{cpf_nove_digitos}{primeiro_digito}{segundo_digito}'

print(cpf_gerado_pelo_calculo)
