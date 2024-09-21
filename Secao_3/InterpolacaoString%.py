# Interpolação
# s - string
# d e i - int
# f - float
# x e X Hexadecimal (ABCDEF0123456789)

nome = 'Bruno'
preco = 1000.9584283
variavel = 'Bruno, o preco total foi R$1000.95'
print(variavel)
variavel = '%s, o preco total foi R$' % nome
print(variavel)
variavel = '%s, o preco total foi R$%f' % (nome, preco)
print(variavel)
variavel = '%s, o preco total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hecadecimal de %d é %x' % (1500, 1500)) 
print('O hecadecimal de %d é %04x' % (1500, 1500)) 