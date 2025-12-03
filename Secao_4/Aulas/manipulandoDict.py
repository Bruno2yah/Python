# Manipulando chaves e valores em dicionários
# criando um dict
pessoa = {}

## 
## 

# Criando chaves dinamicamentes
chave = 'nome'

# Adcionando uma chave ao dict
pessoa[chave] = 'Emily'

pessoa['sobrenome'] = 'Pereira'

# Deletando uma chave no dict
del pessoa['sobrenome']

print(pessoa)
print(pessoa[chave])

# o get serve para verificar se existe uma chave no dict sem quebrar o código
if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print('Existe')