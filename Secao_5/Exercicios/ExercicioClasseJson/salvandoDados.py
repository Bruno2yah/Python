# Exercicio - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instancias
# da classe com os dados salvos 
# Faça em arquivos separados

import json
import Jogo as jogo



caminhoArquivo = 'C:\\Users\\Dell\\Documents\\Estudo\\Cursos\\Udemy\\Python\\Secao_5\\Exercicios\\ExercicioClasseJson\\'
nomeArquivo = 'jogo.json'
caminhoArquivo += nomeArquivo
jogoAtual = ''

try:
    with open(caminhoArquivo, 'r', encoding='utf8') as arquivo:
        jogos = json.load(arquivo)
        ultimoJogo = '' 
        for valor in jogos:
            ultimoJogo = valor
        ultimoJogo = ultimoJogo.split(' ')
        numeroJogo = ultimoJogo[1]
        numeroJogo = int(numeroJogo)
        jogoAtual = f'Jogo {numeroJogo + 1}'
        print(jogoAtual)
except FileNotFoundError:
    jogos = {}
    jogoAtual = 'Jogo 1'
    print('Base de dados ainda não foi criada')

jogo = jogo.Jogo('Dark Souls Remastered', 'Souls like', 'Steam')
jogos[jogoAtual] = jogo.__dict__

with open(caminhoArquivo, 'w', encoding='utf8') as arquivo:
        json.dump(
        jogos, # o valor que deseja colocar
        arquivo, # o arquivo que abriu
        ensure_ascii=False, # irá formatar no estilo json
        indent=2, # irá identar um embaixo do outro
        )

print(f'Adicionado {jogo.nome}')