"""
Exiba os índices da lista
0 Maria
1 Helena 
2 Bruno
"""
import os 
os.system('cls')

lista = ['Maria', 'Helena', 'Bruno']
indice = 0
for nome in lista:
    print(indice, nome)
    indice += 1