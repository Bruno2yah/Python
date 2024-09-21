"""
Iterando strings com while
"""
nome = 'Bruno'
tamanho_nome = len(nome)
contador = 0
string = ''
while contador < tamanho_nome:
    string += f'*{nome[contador]}'
    contador += 1
string += '*'
print(string)