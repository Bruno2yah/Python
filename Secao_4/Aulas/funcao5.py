"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar
falarBomDia = criar_saudacao('bom dia')
falarBoaNoite = criar_saudacao('boa noite')

for nome in ['Maria', 'Joana', 'Luiz', 'Emily', 'Bruno']:
    print(falarBomDia(nome))