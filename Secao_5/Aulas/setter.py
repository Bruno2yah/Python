"""
@property + @setter - getter e setter no modo Pythônico
- como getter
- ´p/ evitar quebrar o código cliente 
- p/ habilitar setter 
- p/ executar ações ao obter um atributo
Atributos qeu começam com um ou dois underlines não devem ser usados fora da classe
"""

class Caneta:
    def __init__(self, cor):
        self._cor = cor 

    # getter
    @property 
    def cor(self):
        return self._cor
    
    # setter de cor
    @cor.setter
    def cor(self, cor):
        self._cor = cor

caneta = Caneta('azul')

# mostrando valor do atributo
print(caneta.cor)

# alterando o valor usando o setter
caneta.cor = 'rosa'

print(caneta.cor)