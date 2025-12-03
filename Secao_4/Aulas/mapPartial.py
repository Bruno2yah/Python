# map - para mapear dados 

import functools

def printIter(iterator):
    print(*list(iterator), sep='\n')

def aumentarProcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

def mudaPrecoProduto(produto):
    return {
        **produto, 'preco': aumentarDezPorcento(produto['preco'])
    }

aumentarDezPorcento = functools.partial(aumentarProcentagem, porcentagem=1.1) # usando essa função cria uma closure

produtos = [
    {'nome': 'Produto 1', 'preco': 20,},
    {'nome': 'Produto 2', 'preco': 10,},
    {'nome': 'Produto 3', 'preco': 30,},
    {'nome': 'Produto 4', 'preco': 50,},
    {'nome': 'Produto 5', 'preco': 40,},
]

# novosProdutos = [
#     {**p, 'preco': aumentarDezPorcento(p['preco'])} for p in produtos
# ]

novosProdutos = map(mudaPrecoProduto, produtos)

printIter(novosProdutos)