"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
import os

os.system('cls')

# nome = 'Bruno'
# outra_variavel = nome
# nome = 'Emily'
# print(nome)
# print(outra_variavel)

lista_a = ['Bruno', 'Emily']
lista_b = lista_a # aponta para o mesmo valor na memória

lista_a[0] = 'Qualquer coisa'
print(lista_b)

lista_c = ['Bruno', 'Emily']
lista_d = lista_c.copy() # copia os valores

lista_c[0] = 'Qualquer coisa'
print(lista_d)