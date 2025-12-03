# Introdução ás generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
    yield 1 # pausar
    print('continuando...')
    yield 2 # pausar
    print('Mais uma vez..')
    yield 3

gen = generator(n=0)
print(gen)
print(next(gen))
print(next(gen))