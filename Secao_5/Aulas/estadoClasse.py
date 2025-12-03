# Mantendo estados dentro da Classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def pararfilmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return
        print(f'{self.nome} está parando de filmar')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        print(f'{self.nome} está fotografando...')
        

camera1 = Camera('Canon')
camera2 = Camera('Sony')
camera1.filmar()
print(camera1.filmando)
print(camera2.filmando)

