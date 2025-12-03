lista = []

for x in range(3):
    for y in range(3):
        lista.append((x, y))

lista = [
    (x, y) # o que será exibido
    for x in range(3)
    for y in range(3)
]
print(lista)