def unirListas(lista1, lista2):
    contador = 0
    listaFinal = []
    listaParametro = []
    listaSecundaria = []

    if len(lista1) >= len(lista2):
        listaParametro = lista2
        listaSecundaria = lista1
    else:
        listaParametro = lista1
        listaSecundaria = lista2

    for i in listaParametro:
        listaFinal.append((i, listaSecundaria[contador]))
        contador += 1
    return listaFinal

def apresentarLista(lista):
    for linha in lista:
        print(linha)

# Solução professor:
# min() pega o menor valor dos parametros informados
# max() pega o maior valor dos parametros informados

def zipper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2)) # pegando o menor indice entre eles
    return [(lista1[i], lista2[i]) for i in range(intervalo)]



