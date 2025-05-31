"""
Exercicios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parametro
"""

def criarMultiplicador(multiplicador):
    def multiplica(numero):
        return numero*multiplicador
    return multiplica
    
duplicar = criarMultiplicador(2)
triplicar = criarMultiplicador(3)
quadruplicar = criarMultiplicador(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))