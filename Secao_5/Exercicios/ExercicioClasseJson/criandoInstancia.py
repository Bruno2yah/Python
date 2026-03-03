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
        # jogo1 = jogo.Jogo(**jogos)
        jogos = list(jogos.values())
        jogo1 = jogo.Jogo(**jogos[0])
        jogo2 = jogo.Jogo(**jogos[1])
        jogo3 = jogo.Jogo(**jogos[2])
        print(jogo1.nome)
        print(jogo2.nome)
        print(jogo3.nome)
except FileNotFoundError:
    jogos = {}
    print('Base de dados ainda não foi criada')

