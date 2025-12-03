# filter é um filtro funcional

import functools

def printIter(iterator):
    print(*list(iterator), sep='\n')

produtos = [
    {'nome': 'Produto 1', 'preco': 20,},
    {'nome': 'Produto 2', 'preco': 10,},
    {'nome': 'Produto 3', 'preco': 30,},
    {'nome': 'Produto 4', 'preco': 50,},
    {'nome': 'Produto 5', 'preco': 40,},
]

novosProdutos = [
    produto for produto in produtos if produto['preco'] > 30
]

novosProdutos = filter(
    lambda p: p['preco'] > 10, produtos
)

printIter(novosProdutos)