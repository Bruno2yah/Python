"""
method vs @classmethod vd #staticmethod
method - self, método de instancia
@classmethod - cls, método de classe
@staticmethod - método estático (não existe self, não existe cls)
"""
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def setUser(self, user):
        self.user = user

    def setPassword(self, password):
        self.password = password

    @classmethod
    def createWithAuth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def soma(x, y):
        return x + y

c1 = Connection() # instanciou o a classe

c2 = Connection.createWithAuth('Bruno', '1234')

# print(c1.user) # user inicia na classe sendo None
# c1.setUser('Bruno') # altera o valor de user
# c1.setPassword('1234') # altera o valor de user
# print(c1.user) # apresentação da mudança
# print(c1.password) # apresentação da mudança