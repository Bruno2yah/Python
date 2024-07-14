# Operadores lógicos
# and (e) or (ou) not (nao)
# and - todas as condições precisam ser verdadeiras
# se qualquer valor for considerado falso
# a expressao inteira será avaliada naquele valor
# são considerados falsy (que você ja viu)
# 0 0.0 '' False
# Tambem existe o tipo none que é usado para representar um não valor
# or - ou
# Se uma condição for considerada True, realiza o if
# not = usado para inverter expressoes
# not True = False
# not False

entrada = input('[E]ntrar [S]air: ')
senha_permitida = '12345'

if entrada == 'E' or entrada == 'e':
    senha_digitada = input('Digite a senha para entrar:  ')
    if((entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida):
        print('Entrou')
    else:
        print('Senha invalida')
        print('Saiu')
else:
    print('Sair')

print(True and True and True)
print(True and False and True) 
print(bool(''))
print(bool(' '))
if 0 and 1:
    print(True and 1)

senha = input('Senha: ') or 'Sem senha'

# not
senha = input('Senha: ')

if not senha:
    print('Voce não digitou nada')

print(not True)
print(not False)
print(not 1)
print(not 0)
