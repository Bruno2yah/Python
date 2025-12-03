# operadores in e not in 
# Strings são iteráveis
# 0 1 2 3 4 
# B r u n o
#-5-4-3-2-1
nome = 'Bruno'
print(nome[2])
print(nome[-3])

print('r' in nome)
print('r' not in nome)
print(10 * '-')
print('z' in nome)
print('z' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que seseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
