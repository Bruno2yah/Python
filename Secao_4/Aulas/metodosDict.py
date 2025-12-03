"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores 
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

import copy

pessoa = {
    'nome': 'Emily',
    'sobrenome': 'Pereira',
}

# metodo pouco utilizado e de dificil leitura
print(pessoa.__len__())

# metodo mais utilizado e facil leitura
print(len(pessoa))

# Retorna um dicionario com as chaves
print(pessoa.keys())

# Retorna um dicionario com os valores
print(pessoa.values())

# Retorna um dicionario com a chave e o valor
print(pessoa.items())

# De padrao o python converteria apenas as chaves e colocaria em um index
print(list(pessoa))

# armazena a chave e o valor no index
print(list(pessoa.items()))

# De padrao o python retorna chaves
for chave in pessoa:
    print(chave)

# utilizando essa função retorna os valores
for valor in pessoa.values():
    print(valor)

# utilizando essa função retorna chaves e valores
for chave, valor in pessoa.items():
    print(chave, valor)

# isso serve para deixar um valor padrão caso não tenha no dicionario
pessoa.setdefault('idade', 12) # primeiro parametro é a chave, segundo parametro é o valor
print(pessoa['idade'])

d1 = {
    'c1': 1,
    'c2': 1,
}

# Note que atribuir d1 para a variavel d2 não faz uma cópia, apenas faz d2 apontar para o mesmo valor 
# que d1 está apontando
d2 = d1

# o que significa que alterar o valor de c1 em d2 faz com que ocorra mudanças em d1
d2['c1'] = 100

# Note que alterar o valor de c1 da variavel d2 alterou o valor em d1
print(f'O valor de D1 {d1}')

d3 = {
    'c1': 2,
    'c2': 3,
    'l1': [0, 1, 2, 3]
}

# Note que por sua vez, ao atribuir utilizando o método copy, faz com que crie outro dict copiando todos
# Os valores MU
d4 = d3.copy()

# Então alterando o valor em d4, não altera d3
d4['c1'] = 100

# Porém se trata de uma shallow copy, ou seja, uma cópia rasa, ele não copia valores mutáveis
d4['l1'][1] = 100
print(f'O valor de d4 {d4}')
print(f'O valor de d3 {d3}')

d5 = {
    'c1': 2,
    'c2': 3,
    'l1': [0, 1, 2, 3]
}

# Importando o módulo copy e utilizando o metodo deepcopy, copia até mesmo os dados mutáveis
d6 = copy.deepcopy(d5)


d6['c1'] = 100

d6['l1'][1] = 100
print(f'O valor de d6 {d6}')
print(f'O valor de d5 {d5}')


p1 = {
    'nome': 'Emily',
    'sobrenome': 'Pereira',
}

# caso tenha a chave nome executa o falor, caso não, executa o parametro atribuido
print(p1.get('nome', 'Não existe'))

# pop ele pega o valor de uma chave determinada, ao mesmo tempo que exclui ela
sobrenome = p1.pop('sobrenome')
print(sobrenome)
print(p1)

p1['sobrenome'] = 'Pereira'
print(p1)

# popitem ele pega a ultima chave adicionada, exclui ela, e adiciona a variavel
ultimaChave = p1.popitem()
print(ultimaChave)
print(p1)

# Update serve para atualizar um dict
p1.update({
    'sobrenome': 'Pereira',
    'idade': 18,
    'sexualidade': 'Hétero'
})

# Também é possivel atualizar desta forma
p1.update(genero='Mulher', profissão='Modelo')

# Também é possivel atualizar ultilizando tuplas
tupla = (('escolaridade', 'Ensino Médio'), ('nacionalidade', 'Brasileira'))
# também é possivel utilizar listas
lista = [['escolaridade', 'Ensino Médio'], ['nacionalidade', 'Brasileira']]
p1.update(tupla)
print(p1)