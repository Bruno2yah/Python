# @staticmethod (métodos estáticos) são inúteis em Python 
# métodos estáticos são métodos que estão dentro da classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua classe.

class Classe:
    @staticmethod
    def funcaoClasse():
        print('oi')

c1 = Classe()
c1.funcaoClasse()