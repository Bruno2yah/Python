"""
Introdução às funções (def) em Python
Funcções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam none (nada).
"""
# def Print():
#     print('Várias')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c):
#     print(a, b,c)
# imprimir(1, 2, 3) 
# imprimir(4, 5, 6) 

def saudacao(nome='Sem nome'): #se nao passar nem um valor, o argumento ganha o valor de "Sem nome"
    print(f'Olá, {nome}')

saudacao('Bruno')
saudacao('Emily')
saudacao('Eliana')