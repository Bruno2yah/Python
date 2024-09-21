"""
enumerate - enumera iteráveis (Índices)
"""
import os
os.system('cls')
lista = ['Maria', 'Emily', 'Bruno']
lista.append('Neymar')

lista_enumerada = enumerate(lista)
print(lista_enumerada)

for item in lista_enumerada:
    print(item)
print(20*'-')

# vai ter gasto todo o iterator então não vai retornar nada
for item in lista_enumerada:
    print(item)

# se declarar direto no for, ele vai criar toda vez, então da para criar quantos for quiser
for item in enumerate(lista):
    print(item)
print(20*'-')
for item in enumerate(lista):
    print(item)
print(20*'-')
for item in enumerate(lista):
    print(item)
print(20*'-')

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)
print(20*'-')

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)
print(20*'-')

for indice, nome in enumerate(lista):
    print(indice, nome)
print(20*'-')

for tupla in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla:
        print(f'\t{valor}')