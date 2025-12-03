"""
split e join com list e str
split - divide uma string
join - une uma string
"""
import os
os.system('cls')
frase = "Olha só que, coisa interessante"
lista_palavras = frase.split()
print(lista_palavras)

lista_palavras_2 = frase.split(',')
print(lista_palavras_2)

lista_palavra_2_fixed = []
for i, frase in enumerate(lista_palavras_2):
    lista_palavra_2_fixed.append(lista_palavras_2[i].strip())
print(lista_palavra_2_fixed)

frases_unidas = '-'.join('abc') # tem que ser uma string --- o o primeiro valor é oq vc deseja separar o que está dentro do segundo
print(frases_unidas)

frases_unidas = ', '.join(lista_palavra_2_fixed)
print(frases_unidas)