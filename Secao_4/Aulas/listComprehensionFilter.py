# O que vem a esquerda do for é mapeamento
# O que vem a direita do for é filtro
# Mapeamento significa que a lista original e a nova lista terão o mesmo tamanho
# Filtro significa que voce pode ou não incluir o valor

import pprint

def printPersonalizado(valor):
    pprint.pprint(valor, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novosProdutos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

printPersonalizado(novosProdutos)

# Dessa forma é filtrado o que será colocado na lista
lista = [n for n in range(10) if n < 5]
print(lista)