def adicionarLista(valor, listaAdicionar):
    listaAdicionar.append(valor)

def removerLista(lista, apagado):
    apagado.append(lista[-1])
    lista.pop()

def refazerLista(lista, apagado):
    lista.append(apagado[-1])
    apagado.pop()