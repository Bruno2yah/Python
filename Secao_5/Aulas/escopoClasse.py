# Escopo da classe e de métodos da classe
class Animal:
    # qualquer variavel fica no escopo
    def __init__(self, nome):
        self.nome = nome

leao = Animal(nome='Leão')