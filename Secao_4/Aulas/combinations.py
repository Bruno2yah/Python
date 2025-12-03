"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa - iterável + tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores unicos
"""

import itertools

def printIter(iterator):
    print(*list(iterator), sep='\n') # convertendo em lista ja faz dar varios next, e armazenar o iterator na lista sem dar for
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia'
]

camisetas = [
    ['Preta', 'Branca'],
    ['M', 'P', 'G'],
    ['Masculino', 'Feminino', 'Unisex'],
    ['Algodão', 'Poliéster']
]
# combinations(variavel, grupos que irao separar)
combinacaoPessoasGrupos2 = itertools.combinations(pessoas, 2) # irá gerar um iterator
permutacaoPessoasGrupos2 = itertools.permutations(pessoas, 2) # irá gerar um iterator

print('Utilizando combinations:')
printIter(combinacaoPessoasGrupos2) 
print('Utilizando permutations:')
printIter(permutacaoPessoasGrupos2) 

# combina mais de um valor
combinacaoCamisetas = itertools.product(*camisetas)

print('Utilizando product:')
printIter(combinacaoCamisetas)