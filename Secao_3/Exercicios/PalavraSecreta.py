"""
Faça um jogo para o usuário advinha qual a palvra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está
na palavra secreta
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário
"""
import os

palavra_secreta = 'Bruno'
palavra_mostrada = ''
respostas_certas = ''
tentativas = 0

os.system('cls')
while True:
    letra_resposta = input('Digite uma letra: ')
    tentativas += 1 
    if len(letra_resposta) > 1:
        print('Digite apenas uma letra')
        continue
    if letra_resposta.lower() in palavra_secreta.lower() and letra_resposta.lower() not in respostas_certas.lower():
        respostas_certas += letra_resposta
        palavra_mostrada = ''
        for i in palavra_secreta:
            contador = 0
            for resposta in respostas_certas:
                if i.lower() == resposta.lower():
                    palavra_mostrada += i
                    contador += 1
            if contador == 0:
                palavra_mostrada += "*"
    elif palavra_mostrada == '':
        palavra_mostrada = len(palavra_secreta)*'*'

    print(f'Palavra secreta: {palavra_mostrada}')
    if palavra_mostrada == palavra_secreta:
        print(f'A plavra secreta era: {palavra_secreta}\nVocê concluiu em {tentativas} tentativas')
        break