"""
Faça uma lista de comprar com listas
o usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
não permita que o programa quebre com erros de indices inexistentes na lista
"""
import os
os.system('cls')
lista = []
while True:
    acao = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar [e]ditar:\n').lower()
    if acao == 'i':
        while True:
            item = input('Insira o item:\n').capitalize()
            if item:
                lista.append(item)
                os.system('cls')
                break
            else:
                print('Valor incorreto.\n')
                continue
    elif acao == 'a':
        while True:
            indice = input('Digite o indice do item:\n')
            if indice:
                try:
                    indice = int(indice)
                    del lista[indice]
                    os.system('cls')
                    break
                except:
                    print('Não existe esse indice na lista.')
                    continue
            else:
                print('Valor vazio.')
                continue
    elif acao == 'l':
        if lista:
            for indice, nome in enumerate(lista):
                print(indice, nome)
            continue
        else:
            print('Lista vazia.')
            continue
    elif acao == 'e':
        while True:
            indice = input('Digite o indice do item que deseja editar:\n')
            valor = input('Digite o novo valor:\n')
            if indice and valor:
                try:
                    indice = int(indice)
                    lista[indice] = valor
                    break
                except:
                    print('Indice não existe')
                    continue
            else:
                print('Valor vazio.')
                continue
    elif acao == 's':
        break
    else:
        print('Valor incorreto.')
        continue