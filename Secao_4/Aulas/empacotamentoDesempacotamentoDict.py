# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a
print(a, b)

# é possivel fazer o desempacotamento com dict
# Sempre que está tirando do dict é desempacotamento
# Sempre que está colocando no dict é empacotamento

pessoa = {
    'nome': 'Emily',
    'sobrenome': 'Pereira'
}

# Assim como no for, o valor que o dict atribui de padrão, é da key
nome, sobrenome = pessoa

print(nome, sobrenome)

# Dessa forma ele passa somente o valor
nome, sobrenome = pessoa.values()

print(nome, sobrenome)

# Também é possivel passar uma tupla com tanto a key quanto o valor
nome, sobrenome = pessoa.items()

print(nome, sobrenome)

# Também é possivel desempacotar internamente
(a1, a2), (b1, b2) = pessoa.items()
print(f'Chave: {a1} Valor: {a2}\nChave: {b1} Valor: {b2}')

# Essa é outra forma de desempacotar
for chave, valor in pessoa.items():
    print(chave, valor)

# Agora e se existe um outro dict
dadosPessoa = {
    'idade': 18,
    'altura': 1.69
}

# como juntar esses dois dicts?
print(f'Dict pessoa: {pessoa} dict dados: {dadosPessoa}')

# uma das formas seriam criar um novo dict extraindo
# ultilizando ** se extrai o dict
# desta forma a variavel pessoa completa, atribui todas chaves e valores de dict pessoa
# assim se tornando dict pessoaCompleta
# tambem é possivel adicionar mais chaves e valores
# Também é possivel se extrair quantos dicts quiser
# assim sendo, juntando os dois dicts
pessoaCompleta = {**pessoa, **dadosPessoa, 'Cabelo': 'ondulado'}

print(pessoaCompleta)

# args e kwargs 
# args seriam os argumentos não nomeados - *args
# kwargs - keyword arguments, seriam os argumentos nomeados - **kwargs

# Todos os dados  não nomeados que forem passados na function, irão para o parametro args
# Todos os dados nomeados irão para o parametro kwargs
def mostroArgumentosNomeados(*args, **kwargs):
    print(f'Argumentos não nomeados: {args}')
    print(f'Argumentos nomeados: {kwargs}')

n1, n2, n3, n4 = 1, 2, 3, 4


# desta forma os valores das variaveis n, serão armazenados em args
# já os valores do dict pessoa como foi um argumento nomeado iria para kwargs
print(mostroArgumentosNomeados(n1, n2, n3, n4, pessoa=pessoaCompleta))