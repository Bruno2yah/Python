"""
class - Classes são moldes para criar novos objetos
As classes gera novos objetos (instâncias) que 
podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados 
internos para realizar várias ações.
por convenção, usamos pascalCase para nomes de classes.
"""
# string = 'luiz' # str

# print(string.upper())
# print(f'String é uma instancia da classe str? {isinstance(string, str)}')

class Pessoa:
    def __init__(self, nome, sobrenome): # sempre reservar o primeiro parametro para self
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Bruno', 'Geanini')
# p1.nome = 'Bruno'
# p1.sobrenome = 'Geanini'

p2 = Pessoa('Emily', 'Pereira')
# p2.nome = 'Emily'
# p2.sobrenome = 'Pereira'

print(f'Pessoa 1:\nNome: {p1.nome}\nSobrenome: {p1.sobrenome}\n')
print(f'Pessoa 2:\nNome: {p2.nome}\nSobrenome: {p2.sobrenome}')