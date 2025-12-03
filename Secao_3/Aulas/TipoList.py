"""
Listas em python
Tipo list - mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#        +01234
#        -54321
string = 'ABCDE'

# lista pode ser escrita de duas maneiras
lista2 = list() # serviria também para converter algo em lista
lista = [] # é criar uma lista vazia, se comparar no bool retorna false
# print(type(lista), type(lista2))

#         0     1      2      3   4     indices
lista = [123, True, 'Bruno', 1.2, []] # pode conter todos os tipos, ela pode ter lista dentro da lista
lista[2] = 'Emily'
print(lista)