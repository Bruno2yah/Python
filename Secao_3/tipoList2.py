"""
Listas em python
Tipo list - mutável
Suporta vários valores de qualquer tipo 
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
create read update delete
criar, ler, alterar, apagar = lista[i] (CRUD)
É interessante só mexer com os dados do final, pq senão requer muito processamento
"""
import os

os.system('cls')

lista = [10, 20, 30, 40] # CREATE
lista[2] = 300 # UPDATE
del lista[1] # DELETE
print(lista) # READ

lista.append(50) # Adciona mais um valor ao final da lista
lista.pop() # remove o ultimo valor da lista, no momento o ultimo valor é o 50
lista.append(60) # Adciona mais um valor ao final da lista
lista.append(70) # Adciona mais um valor ao final da lista
lista.append(80) # Adciona mais um valor ao final da lista
ultimo_valor = lista.pop() # ele remove e ainda retorna o ultimo valor
lista.pop(1) # pode passar o indice dentro do metodo pop para apaga-lo
print(f'{lista} removido {ultimo_valor}')