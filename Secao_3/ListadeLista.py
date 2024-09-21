"""
Lista de listas
"""
import os
os.system('cls')

salas= [
    ['Maria', 'Helena'],
    ['Helaine'],
    ['Bruno', 'Emily', 'Eliana', (0, 10, 20, 30, 40)]
]

print(salas[2][1])
print(salas[0][1])
print(salas[2][3][2])

for sala in salas:
    for aluno in sala:
        print(aluno)