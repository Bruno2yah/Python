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

lista = [10, 20, 30, 40]
lista.append('Bruno')
nome = lista.pop()
lista.append(1234)
del lista[-1]
# lista.clear() # Limpa a lista
lista.insert(0, 5) # o primeiro argumento é o indice que deseja, o segundo é o valor
print(lista)