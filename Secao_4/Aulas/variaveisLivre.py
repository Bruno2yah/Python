# variáveis livres + nonlocal (locals, globais)

# print(globals())# Retorna tudo que está definido global

def fora(x):
    a = x # na função "dentro"  a variavel "a" é uma variavel livre
    
    def dentro():
        # print(locals()) # serve para ver as variaveis locais
        print(dentro.__code__.co_freevars) # Retorna as variaveis livres da função dentro
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())

def concatenar(stringInicial):
    valorFinal = stringInicial
    def interno(valorConcatenar=''):
        # como é uma variavel livre, para acessa-la dentro da variavel interno
        # é necessario defini-la como "nonlocal" para poder altera-la
        nonlocal valorFinal
        valorFinal += valorConcatenar
        return valorFinal
    return interno

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

final = c()
print(final)