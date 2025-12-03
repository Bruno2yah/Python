# List comprehension em Python
# Lista comprehension é uma forma rápida para criar listas
# a partir de iteráveis
# print(list(range(10)))

lista = []

for numero in range(10):
    lista.append(numero)

print(lista)

# outra forma seria utilizar um for dentro da lista
# Antes do For vai o que você deseja que seja incluido
# ex: 1 for numero in range(10) irá colocar o numero 1 (10 vezes)
lista2 = [numero for numero in range(10)]
print(lista2)

# é Possivel utilizar qualquer tipo de operação , inclusive condições ternárias
lista3 = [
    numero * 2
    for numero in range(10)
]

print(lista3)