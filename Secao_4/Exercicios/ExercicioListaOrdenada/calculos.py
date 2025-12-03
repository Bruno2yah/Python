import copy

# Criei minha propria funcao para fazer a copia profunda
def copiaProfunda(lista): 
    return copy.deepcopy(lista)

# Essa função serve para ordenar uma lista de dict ou tuplas
# em ordem crescende ou decrescente
# parametro lista, é a lista a ser recepcionada
# parametro valorOrdem é a chave que será utilizada para ordenar
# parametro direcaoOrdem é para definir a ordem nos seguintes fatores
# False = crescente, True Decrescente
# Definido desse jeito, caso o usuario nao definir a ordem, é padrão crescente
def ordenandoLista(lista, valorOrdem, direcaoOrdem=False):
    # fazendo uma copia profunda
    novaLista = copiaProfunda(lista)
    # aqui está sendo ordenada a lista
    novaLista.sort(key=lambda item: item[valorOrdem], reverse=direcaoOrdem)
    return novaLista

# Funcao para aumentar ou diminuir um valor na lista
# Parametro lista, é a lista a ser recepcionada
# Parametro valorAlteracao, é a chave que será alterada
# Parametro numeroAjuste, é a porcentagem que irá aumentar ou diminuir
def alterarValorTodosItems(lista, valorAlteracao, numeroAjuste):
    # fazendo a copia profunda
    novaLista = copiaProfunda(lista)
    # Laço de repetição para pegar cada linha da lista
    for i in novaLista:
        # aqui está sendo atribuido o novo valor
        i[valorAlteracao] = round(i[valorAlteracao]*numeroAjuste, 2) # O round arredonda os valores para a casa definida pos ,
    return novaLista