# try, except, else e finally
# Erros em python são classes
# except trata esses erros
# a classe Exception serve para todos os erros

a = 18
b = 1

try:
    c = a/b
    print('linha'[1000])
except ZeroDivisionError: # após o except pode se colocar o error especifico
    print('Dividiu por zero')
except NameError:
    print('Não definiu a variavel')
except (TypeError, IndexError) as error: # é possivel mandar uma tupla, utilizando as e passando uma variavel é possivel caputrar a mensagem de erro
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome: ', error.__class__.__name__) # assim é possivel exibir o nome do erro
except Exception:
    print('ERRO desconhecido')

print('Continuar')