"""
Listas em python
Tipo list - mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: 
    append - adciona um item ao final da lista
    insert - adciona um item no indice escolhido
    pop - remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas

create read update delete
criar, ler, alterar, apagar = lista[i] (CRUD)
É interessante só mexer com os dados do final, pq senão requer muito processamento
"""

import os

os.system('cls')

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # extend não retorna nada, ele mexe direto na lista a
print(lista_c)
print(lista_d) # por não retornar nada, a lista d recebe None
print(lista_a)