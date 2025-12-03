"""
Criando arquivos com Python
Usamos a função open para abrir 
um arquivo em python (ele pode ou não existir)
Modos:
r (leitura), w (escrita), x (para criação)
a (escreve ao final), b (binário)
t (modo texto), + (leitura e escrita)
context manager - with (abre e fecha)
Métodos úteis
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas )
vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo 
Vamos falar mais sobre o módulo json, mas: 
json.dump = gera um arquivo json 
json.load
"""

import os 

caminhoArquivoCompleto = 'C:\\Users\\Dell\\Documents\\Estudo\\Cursos\\Udemy\\Python\\Secao_4\\Aulas\\'
caminhoArquivo = 'aula116.txt'
caminhoArquivoCompleto += caminhoArquivo

# sempre que abrir um arquivo, fechar ele logo em seguida
# arquivo = open(caminhoArquivoCompleto, 'w')
# arquivo.close()

#dessa forma o arquivo é fechado automaticamente 
#dessa forma eu consigo escrever no arquivo
#utilizando enconding caracteres serão reconhecidos
with open(caminhoArquivoCompleto, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Emily meu amor\nCorinthians minha vida')

# com o 'a' ele adiciona escrita no final, mantendo salvo, enquanto o w sobrescreve
# with open(caminhoArquivoCompleto, 'a') as arquivo:
#     arquivo.write('Emily meu amor\nCorinthians minha vida')

# dessa forma consigo ler o arquivo
with open(caminhoArquivoCompleto, 'r') as arquivo:
    print(arquivo.read())

#remove arquivo
# os.remove(caminhoArquivoCompleto)
# os.unlink(caminhoArquivoCompleto)

os.rename(caminhoArquivoCompleto, 'Aprendendo sobre create em py.txt')