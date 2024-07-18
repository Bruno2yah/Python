frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum'.lower()

i = 0
letra_mais_apareceu = ''
quantidade_letra_mais_apareceu = 0

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    if quantas_vezes_letra_apareceu > quantidade_letra_mais_apareceu and letra_mais_apareceu != letra_atual and letra_atual != ' ':
        quantidade_letra_mais_apareceu = quantas_vezes_letra_apareceu
        letra_mais_apareceu = letra_atual
    elif quantas_vezes_letra_apareceu == quantidade_letra_mais_apareceu and letra_atual not in letra_mais_apareceu:
        letra_mais_apareceu += ', ' + letra_atual
    i+=1
print(f'O caractere que mais apareceu é: "{letra_mais_apareceu}" aparecendo {quantidade_letra_mais_apareceu} vezes')