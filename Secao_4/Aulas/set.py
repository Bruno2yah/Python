"""
Sets - Conjuntos em Python (tipo set)
conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.htm
Representados graficamento pelo diagrama de Venn 
Sets em Python são mutáveis, porém aceitam apenas 
tipos imutáveis como valor interno

Criando um set
set(iterável) pu {1, 2, 3}

Sets dão eficientes para remover valores duplicados de iteráveis.
- eles não tem índexes;
- eles não garantem ordem;
- eles são iteráveis (for, in, not in)

Métodos úteis: 
add, update, clear, discard
"""
# ele vai iterar dados aqui dentro
set1 = set('Emily')
# set1 = {'Emily', 1, 2, 3, 4}  # ele vai criar um set com dados
print(set1, type(set1))

# os set naturalmente eliminam valores duplicados
listaValoresDuplicados = [1, 2, 3, 4, 4, 4, 4, 5, 2, 1]
set2 = set(listaValoresDuplicados)
print(set2, type(set2))
# assim da para remover valores repetidos em uma lista de forma rapida
listaValoresUnicos = list(set2)
print(listaValoresUnicos, type(listaValoresUnicos))

# Métodos
set3 = set() # criando set vazio

# add serve para adicionar valores ao set, porém só aceitam um valor
set3.add('Emily')
set3.add('Bruno')
set3.add(1)
# set3.add(1, 2) por passar mais de um valor, dá erro
print(set3)

# update serve para atualizar, se colocar um nome, ele irá iterar, mas com ele voce pode passar iteraveis
set3.update('Amor') # dessa forma irá iterar a palavra
set3.update(('Amor', 'Love', 1, 2, 3, 4, 5)) # passando um iterável irá atualizar varios valores de uma vez
print(set3)

# discard irá apagar valores do set, e você tem que passar o valor em si como parametro
set3.discard('Bruno')
set3.discard(1)
set3.discard((2, 3, 4, 5)) # não funciona utilizar tupla para apagar varios valores de uma vez
print(set3)

# clear irá limpar o set, apagando todos os valores
set3.clear() 
print(set3)
