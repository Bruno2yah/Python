# Exercicio - lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears 
# todo = [] => lista de tarefas
# todo = ['fazer café] -> adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> adicionar caminhar
# desfazer = ['fazer café'] -> refazer ['caminhar']
# desfazer = [ -> refazer['caminhar', 'fazer café']
# refazer = todo['fazer café']
# refazer = todo['fazer café', 'caminhar']

import calculos
import os
import json

caminhoArquivo = 'C:\\Users\\Dell\\Documents\\Estudo\\Cursos\\Udemy\\Python\\Secao_4\\Exercicios\\ExercicioListaTarefas\\'
nomeArquivo = 'Lista de tarefas.json'
caminhoArquivo += nomeArquivo

tarefas = []
os.system('cls')

try:
    with open(caminhoArquivo, 'r', encoding='utf8') as arquivo:
        tarefas = json.load(arquivo) 
except FileNotFoundError:
    print('Base de dados ainda não foi criada')

apagado = []

while True:
    acao = input('Comandos: listar, desfazer, refazer, clear\nDigite uma tarefa ou comando: ')
    print()
    if acao == 'listar':
        print('Tarefas:')
        for tarefa in tarefas:
            print(tarefa)
        print()
    elif acao == 'desfazer':
        if not tarefas:
            print('nada a ser desfeito')
            print()
            continue
        calculos.removerLista(tarefas, apagado)
        print('Tarefas:')
        for tarefa in tarefas:
            print(tarefa)
        print()
    elif acao == 'refazer':
        if not apagado:
            print('nada a ser refeito')
            print()
            continue
        calculos.refazerLista(tarefas, apagado)
        print('Tarefas:')
        for tarefa in tarefas:
            print(tarefa)
        print()
    elif acao == 'clear':
        os.system('cls')
    elif acao == 'exit':
        break
    elif acao == '' or acao == ' ':
        print('por favor digite um valor válido')
        print()
    else:
        calculos.adicionarLista(acao, tarefas)
        print('Tarefas:')
        for tarefa in tarefas:
            print(tarefa)
        print()
    if not tarefas:
        continue
    with open(caminhoArquivo, 'w', encoding='utf8') as arquivo:
        json.dump(
        tarefas, # o valor que deseja colocar
        arquivo, # o arquivo que abriu
        ensure_ascii=False, # irá formatar no estilo json
        indent=2, # irá identar um embaixo do outro
        )

print('Programa finalizado')