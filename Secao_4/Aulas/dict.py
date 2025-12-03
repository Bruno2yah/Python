"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo 
Par de "chave" e "valor"
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo , incluindo outro dicionário
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável> dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}
"""
# Outra forma de criar a classe dict
# pessoa = dict(nome='Emily', sobrenome='Miranda')

# Criar  classe dict
pessoa = {
    'nome': 'Emily',
    'sobrenome': 'Pereira',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()

for chave in pessoa:
    print(chave, pessoa[chave])
