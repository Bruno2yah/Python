import os
import sys

os.system('cls')

# generator expression, iterables e iterators e Python
iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

# todo generator é um iterator, mas o iterator não é um generator

# Criando a lista assim, fica armazenado tudo na memoria
lista = [n for n in range(10000)]

# criando um generator
generator = (n for n in range(10000))

print(generator)

# utilizando a biblioteca sys, ela tem um metodo chamado
# getsizeof
# onde ele retorna o valor em bytes na memoria

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))