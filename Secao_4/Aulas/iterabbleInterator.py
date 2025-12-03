# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

print(f'Dessa forma voce ve que ele cria meio que um objeto {iterator}')

print(f'Aqui ele mostra o proximo valor a ser exibido "{next(iterator)}"')
print(f'Aqui ele mostra o proximo valor a ser exibido "{next(iterator)}"')
print(f'Aqui ele mostra o proximo valor a ser exibido "{next(iterator)}"')

# iterator não tem acesso a posições, nem ao seu tamanho, ele apenas sabe exibir
# o proximo e o proximo, e quando acabar, ele não conseguira ler os valores novamente