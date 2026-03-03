# Métodos da classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro 
# parâmetro, receberemos a própria classe

class Pessoa:
    ano = 2025 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod # isso faz com que o metodo possa ser utilizado direto na classe 
    def metodoClasse(cls):
        print('hey')

    @classmethod 
    def criar50anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod 
    def criarSemNome(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa('Bruno', 21)
p2 = Pessoa.criar50anos('Cristiano')
p3 = Pessoa.criarSemNome(19)
print(Pessoa.ano)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

Pessoa.metodoClasse()