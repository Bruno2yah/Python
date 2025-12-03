# Decoradores com parâmetros
def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('Aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada

@decoradora 
def soma(x, y):
    return x + y

dezMaisCinco = soma(10, 5)
print(dezMaisCinco)