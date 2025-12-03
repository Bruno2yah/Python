def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def criaMultiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# criando a função soma como lambda
# lambda seria como def
# o primeiro x e y o nome dos parametros
# o segundo x e y o que vai ser retornado
# após a virgula seria os parametros
print(executa(lambda x, y: x + y, 2, 3))

# Criando a função cria multiplicador em lambda
# não recomendado pois prejudica a elegibilidade do código
# nesse caso o primeiro lambda está retornando outra função
# O parametro que tem que ser declarado é o do primeiro lambda
# Pois o segundo, deve ser declarado, na chamada da função
duplica = executa(lambda m: lambda n: n*m, 2)

# declarando os parametros da função interna
print(duplica(5))

# criando uma soma de todos os valores chamados com lambda
print(executa(lambda *args: sum(args), 1,2,3,4,5,6,7))