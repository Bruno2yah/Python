"""
continue -> pula para o inicio do laço, ignorando o que vem dps
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador >= 10 and contador <=20:
        print(f'Não vou mostrar o contador {contador}')
        continue

    print(contador)

    if contador == 40:
        break
print('acabou')