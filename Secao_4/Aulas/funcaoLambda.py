"""
Função lambda em Python
A função lambda é uma função como qualquer 
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudp deve ser contido dentro de uma única expressão.
"""
listaNomes = [
    {'nome': 'Emily', 'sobrenome': 'Pereira'},
    {'nome': 'Bruno', 'sobrenome': 'Geanini'},
    {'nome': 'Lionel', 'sobrenome': 'Messi'},
    {'nome': 'Son', 'sobrenome': 'heung min'},
    {'nome': 'Marcos', 'sobrenome': 'Reus'},
]
listaNomes2 = [
    {'nome': 'Emily', 'sobrenome': 'Pereira'},
    {'nome': 'Bruno', 'sobrenome': 'Geanini'},
    {'nome': 'Lionel', 'sobrenome': 'Messi'},
    {'nome': 'Son', 'sobrenome': 'heung min'},
    {'nome': 'Marcos', 'sobrenome': 'Reus'},
]

lista = [3, 32, 1, 34, 5, 6, 6, 21]
print(f'Lista sem ordenar: {lista}')

# ordena a lista
lista.sort()
print(f'Lista em ordem crescente: {lista}')

# Ordena decrescente
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')

# metodo sorted cria um shallow copy
# sorted(lista)

# quando se trata de dicionarios, o python não conseguer ler diretamente
# então tem que criar uma function, que direcione para o python
# O python reconhece o que deve ordenar pelo return
def ordena(item):
    return item['nome']

# A key é onde é onde se deve deixar a function
listaNomes.sort(key=ordena)

print('Utilizando uma função normal')
for item in listaNomes:
    print(item)

# Utilizando a function lambda, é possivel fazer o mesmo que acima
# mas sem definir uma function
# lambda serviria como o nome da function
# o primero item como o parametro
# e o segundo o que deve retornar
# isso altera diretamente a lista
listaNomes2.sort(key=lambda item: item['nome'])

# desta forma cria-se uma nova lista com os valores
listaNomeOrderSobrenome = sorted(listaNomes2, key=lambda item: item['sobrenome'])

print('Utilizando a Funçao Lambda')

for item in listaNomes2:
    print(item)

print(f'Lambda utilizando fazendo deep copy')

for item in listaNomeOrderSobrenome:
    print(item)