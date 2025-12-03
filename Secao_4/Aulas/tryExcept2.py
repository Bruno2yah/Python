# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html

try:
    print('Abrir Arquivo')
    8/0
except ZeroDivisionError:
    print('Dividiu por zero')
else: # Se o código ocorrer sem erros 
    print('Não deu erro')
finally: # Sempre vai ser executado, independente de ter erro ou não
    print('Fechar arquivo')