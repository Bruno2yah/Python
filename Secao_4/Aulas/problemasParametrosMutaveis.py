# Problema dos parâmetros mutáveis em funções Python

def adicionaClientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente1 = adicionaClientes('luiz')
adicionaClientes('Joana', cliente1)
print(cliente1)

cliente2 = adicionaClientes('Helena')
adicionaClientes('maria', cliente2)