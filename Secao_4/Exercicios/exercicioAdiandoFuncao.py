# Exercicio adiando execução de funções
def soma(x, y): 
    return x+y

def multiplica(x, y): 
    return x*y

def executa(funcao, *args):
    argumento1, *_ = args 
    def executaProlongado(argumento2):
        return funcao(argumento1, argumento2)
    return executaProlongado

soma_com_cinco = executa(soma, 5)
multiplica_por_10 = executa(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_10(10))