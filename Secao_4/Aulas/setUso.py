# Exemplo de uso dos set

letras = set()
while True:
    letra = input('Digite: ')
    # Utilizando dessa forma, não importa quantas vezes o usuario digite uma letra, ela nunca vai se repetir
    letras.add(letra)

    if 'l' in letras:
        print('Parabens voce achou a letra misteriosa')
        break

    print(letras)