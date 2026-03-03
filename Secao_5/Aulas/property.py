"""
@property - um getter no modo Pythônico
getter - um método para obter um atributo
cor -> get_cor()
modo pythônico - modo python de fazer coisas
@property é uma propriedade do objeto, ela é um método que se comporta como um atributo
Geralmenteé usada nas seguintes situações:
- como getter
- p/ evitar quebrar código cliente
- p/ habilitar setter
- p/ executar ações ao obter um atributo
código cliente - é o código que usa seu código
"""

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    # outras linguagens de programação
    def get_cor(self):
        return self.cor_tinta
    
    # modo pythonico
    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 'Amarelo'
    
caneta = Caneta('Azul')

print(caneta.get_cor())
print(caneta.cor)
print(caneta.cor_tampa)