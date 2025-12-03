import calculo

"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor
exemplo:
listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]

================== resultado
listaSoma = [2, 4, 6, 8]
"""

listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]

listaSoma = calculo.somandoLista(listaA, listaB)

print(f'minha solução:\n{listaSoma}')

# Solução professor para qualquer linguagem
listaSoma = []
for i in range(len(listaB)):
    listaSoma.append(listaA[i] + listaB[i])
print(f'Solução do professor para qualquer linguagem:\n{listaSoma}')

# Solução utilizando ferramentas do python
listaSoma = []
for i, _ in enumerate(listaB):
    listaSoma.append(listaA[i] + listaB[i])
print(f'Solução utilizando ferramentas do python:\n{listaSoma}')

# A melhor solução utilizando ferramentas python
listaSoma = []
listaSoma = [x + y for x, y in zip(listaA, listaB)]
print(f'A melhor solução utilizando ferramentas do python:\n{listaSoma}')
