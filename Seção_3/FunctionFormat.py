a = 'A'
b = 'B'
c = 1.1
formato = 'a = {} b = {} c = {:.2f}'.format(a, b, c) # python tudo é objetos, então string tem metodos
formato2 = 'a = {0} b = {1} c = {2:.2f}'.format(a, b, c) # podemos utilizar o indices dos parametros
formato3 = 'a = {nome1} b = {nome2} c = {nome3:.2f}'.format(nome1 = a, nome2 = b, nome3 = c) # podemos nomear os parametros

print(formato)
print(formato2)
print(formato3)