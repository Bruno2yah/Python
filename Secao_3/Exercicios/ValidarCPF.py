"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)
    10  9   8   7   6   5   4   3   2
*   5   7   4   4   8   9   7   6   8
    70  36  48  56  12  20  32  27  0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0=301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrario disso:
    resultado é 7
"""
import os
import re
import sys


os.system('cls')
#tratamento do cpf
cpfOriginal = '57448976826'.replace('.', '').replace('-', '')

entrada = input('CPF: ')
cpfOriginal = re.sub(
    r'[^0-9]', # condição
    '', # para o que vai ser trocado
    entrada # valor
)

# string aaa
# ssssss aaa

entrada_e_sequencial = entrada == entrada[0]*len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()
# cpf_list = cpfOriginal.split('-')
# cpf_nove_digitos = cpf_list[0]
# cpf_list = cpf_nove_digitos.split('.')
cpf_nove_digitos = cpfOriginal[:9]
cpf_list = []

soma = 0
i = 10
# soma
for digito in cpf_nove_digitos:
    multiplicacao = int(digito) * i
    soma += multiplicacao
    i -= 1

resultado = (soma*10)%11
primeiro_digito = resultado  if resultado <=9 else 0
print(f'{primeiro_digito=}')

cpf_dez_digitos = cpf_nove_digitos + str(primeiro_digito)

soma = 0
i = 11
for digito in cpf_dez_digitos:
    multiplicacao = int(digito)*i
    soma += multiplicacao
    i -= 1

resultado = (soma*10) % 11
segundo_digito = resultado if resultado <= 9 else 0
print(f'{segundo_digito=}')

cpf_gerado_pelo_calculo = f'{cpf_nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_gerado_pelo_calculo == cpfOriginal:
    print('CPF válido')
else:
    print('CPF inválido')
