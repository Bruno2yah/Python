# groupby - agrupando valores (itertools)

import itertools

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Erica', 'nota': 'B'},
    {'nome': 'Emily', 'nota': 'A'},
    {'nome': 'Bruno', 'nota': 'F'},
    {'nome': 'Lucas', 'nota': 'C'},
    {'nome': 'Amelia', 'nota': 'C'},
    {'nome': 'Jason', 'nota': 'F'},
    {'nome': 'Ajay', 'nota': 'B'},
]

def ordena(aluno):
    return aluno['nota']

alunosAgrupadosOrdem = sorted(alunos, key=ordena)
grupos = itertools.groupby(alunosAgrupadosOrdem, key=ordena) # ordenando pela nota

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)