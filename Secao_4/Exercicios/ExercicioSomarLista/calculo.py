def somandoLista(lista1, lista2):
    intervaloMaximo = zipper(lista1, lista2)
    listaFinal = []
    for i in range(intervaloMaximo):
        resultadoSoma = soma(lista1[i], lista2[i])
        listaFinal.append(resultadoSoma)
    return listaFinal

def zipper(lista1, lista2):
    intervaloMaximo = min(len(lista1), len(lista2))
    return intervaloMaximo

def apresentandoLista(lista):
    for linha in lista:
        print(linha)

def soma(x, y):
    return x+y