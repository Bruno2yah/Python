"""
Exercicio peça ao usuário para digitar seu nome
peça ao usuario para digitar sua idade
se nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        se nome contém (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
Se nada for digitado exiba "Desculpe, você deixou campos vazios"
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
    print(f'O seu nome é {nome}')
    print(f'O seu invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'{nome} contém espaços')
    else:
        print(f'{nome} não contém espaços')
    print(f'O seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[len(nome) - 1]}')
else:
    print('Desculpe, você deixou campos vazios')
    