# Exercicios com funções

# Crie uma função que multiplica todos os argumentos 
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável

def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero 
    return resultado

# Crie uma função fala se um número é par ou ímpar

def seParImpar(num):
    if (num%2 == 0):
        return f'{num} é um número par'
    else:
        return f'{num} é um número ímpar'

print(multiplicacao(3,4,5))
print(seParImpar(10))