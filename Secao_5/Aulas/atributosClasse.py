# Atributos de classe
class Pessoa:
    anoAtual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self):
        return Pessoa.anoAtual - self.idade
    
pessoa1 = Pessoa('Bruno', 21)
pessoa2 = Pessoa('Emily', 19)

print(pessoa1.getAnoNascimento())
print(pessoa2.getAnoNascimento())
