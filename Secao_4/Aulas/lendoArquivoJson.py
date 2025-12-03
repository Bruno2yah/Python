import json

caminhoCompleto = 'C:\\Users\\Dell\\Documents\\Estudo\\Cursos\\Udemy\\Python\\Secao_4\\Aulas\\'
arquivo = 'primeiroSalvarDados.json'
caminhoCompleto += arquivo

with open(caminhoCompleto, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo) 
    print(dados)