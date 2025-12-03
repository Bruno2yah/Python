# Métodos em instancias de classes Python
# Hard coded é algo que foi escrito diretamente no codigo

class Carro:
    def __init__(self, nome='Sem Modelo'):
        self.nome = 'Fusca' # hard coded
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')
celta = Carro('Celta')

print(fusca.nome)
fusca.acelerar()

print(celta.nome)
celta.acelerar()