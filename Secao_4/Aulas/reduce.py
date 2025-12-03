# reduce - faz a redução de um iterável em um valor

import functools

produtos = [
    {'nome': 'Produto 1', 'preco': 20,},
    {'nome': 'Produto 2', 'preco': 10,},
    {'nome': 'Produto 3', 'preco': 30,},
    {'nome': 'Produto 4', 'preco': 50,},
    {'nome': 'Produto 5', 'preco': 40,},
]

total = 0

for produto in produtos:
    total += produto['preco']

print(total)

def funcaoReduce(acumulador, produto):
    # print('acumulador', acumulador)
    # print('produto', produto)
    return acumulador + produto['preco']

totalReduce = functools.reduce(
    funcaoReduce,
    produtos,
    0
)

print(totalReduce)




