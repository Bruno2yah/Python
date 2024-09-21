"""
Introduçãi ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

print(1234)
print(456)
# int('a')

numero = input('Vou dobrar o número que você digitar: ')
print(numero.isdigit()) # isdigit() retorna bool se só tem numeros na variavel, se tiver . pq é float, retorna false

try:
    print('String: ', numero)
    numero_int = int(numero)
    print('Inteiro', numero_int)
    print(f'O dobro de {numero} é {numero_int * 2:.2f}')
except:
    print('Isso não é um número')


#  