"""
For + Range
range -> range(start, stop, step)
"""
numeros = range(10)
print(numeros)
numeros = range(5, 10)
print(numeros)
numeros = range(0, 10, 2)
print(numeros)

for numero in numeros:
    print(numero) # o for não vai pelo indice, ele ja manda o valor, ou seja, não precisa atribuir