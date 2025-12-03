# raise - lançando  exceções (erros)

def NumeroNaoPodeSerZero(numero):
    if numero == 0:
        # Dessa forma reescreve o significado da exception
        raise ZeroDivisionError('Você está tentando dividir por zero')
    
def tipagemIntFloat(numero):
    if not isinstance(numero, (int, float)):
        raise TypeError(f'{numero} deve ser int ou float')


def dividir(numero1, numero2):
    tipagemIntFloat(numero1)
    tipagemIntFloat(numero2)
    NumeroNaoPodeSerZero(numero2)
    return numero1 / numero2

dividir('a', 0)

