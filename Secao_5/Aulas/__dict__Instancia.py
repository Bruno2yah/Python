# __dict__ e vars para atributos de instancia

class Pessoa:
    anoAtual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self):
        return Pessoa.anoAtual - self.idade

dados = {'nome': 'Bruno', 'idade': 21}
pessoa1 = Pessoa(**dados)

# mostram tudo que tem na instancia
print(pessoa1.__dict__) # utilizando pessoa1.__dict__['cor'] = 'Branco' adicionaria um valor a instancia
print(vars(pessoa1))