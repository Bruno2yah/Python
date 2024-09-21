"""
Imprecisão do ponto flutuante
Double-precision floating-point IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal
import os
os.system('cls')
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 3)) # (valor, quantidade de casas decimais) se for 0 não irá aparecer pois arredonda


numero_4 = decimal.Decimal(0.1)
numero_5 = decimal.Decimal(0.7)
numero_6 = numero_4 + numero_5
print(numero_6)

numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
numero_6 = numero_4 + numero_5
print(numero_6)