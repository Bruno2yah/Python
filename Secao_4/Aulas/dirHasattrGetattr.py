# dir, hasattr e getattr em Python
string = 'Emily'

# Strings em python são objetos

# com dir voe consegue ver todos metodos e atributos do objeto
print(dir(string))

print('-'*130)

# hasattr verifica se tem o metodo no objeto
if hasattr(string, 'upper'):
    print('Existe upper')
    print(string.upper())

print('-'*130)

# com o metodo getattr voce consegue acessar o metodo dinamicamente
metodo = 'lower'

if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())