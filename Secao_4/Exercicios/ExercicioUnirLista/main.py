import calculo
import itertools

# Exercicio - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# Listas na ordem
# Use todos os valores da menor lista.
# ex.: 
# ['Salvador', 'Ubatuba', 'belo horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

listaUnida = calculo.unirListas(estados, cidades)
listaUnidaProfessor = calculo.zipper(cidades, estados)
listaUnidaProfessor2 = list(zip(cidades, estados))
listaUnidaProfessor3 = list(itertools.zip_longest(cidades, estados, fillvalue='Sem cidade')) # irá utilizar a lista maior de parametro, e o fillvalue é o valor para quando não ter um item correspondente na outra lista


print('Minha solução:')
calculo.apresentarLista(listaUnida)
print('\nSolução do professor:')
calculo.apresentarLista(listaUnidaProfessor)
print('\nSolução do professor utilizando um metodo que já existe em python:')
calculo.apresentarLista(listaUnidaProfessor2)
print('\nSolução do professor utilizando um metodo que já existe em python,\nmas dessa vez ele está utilizando a lista maior como parametro:')
calculo.apresentarLista(listaUnidaProfessor3)