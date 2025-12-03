"""
Desempacotamento em chamadas de métodos e funções
"""
import os

os.system('cls')
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Emily']
tupla = 'Python', 'é', 'legal'
salas= [
    ['Maria', 'Helena'],
    ['Helaine'],
    ['Bruno', 'Emily', 'Eliana']
]

p, b, *_, u = lista
print(p, u)

# for nome in lista:
#     print(nome, end = ' ')

# print(*lista)
# print(*string)
# print(*tupla)

print(salas)
print(*salas)
print(*salas, sep='\n')
