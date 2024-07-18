"""
Calculadora com while
"""

# # Minha versão
# while True:
#     n1 = input('Qual o primeiro valor: \n')
#     n2 = input('Qual o segundo valor: \n')
#     while True:
#         operacao = input('Qual a operacao:\n 1 - Adição\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n')
#         if operacao == '1':
#             resultado = int(n1) + int(n2)
#             break
#         elif operacao == '2':
#             resultado = int(n1) - int(n2)
#             break
#         elif operacao == '3':
#             resultado = int(n1) * int(n2)
#             break
#         elif operacao == '4':
#             if int(n2) == 0:
#                 resultado = 'Impossivel dividir por 0'
#             else:
#                 resultado = int(n1) / int(n2)
#             break
#         else:
#             print('Operação inválida')
#             continue
#     print(resultado)
#     continuar = input('Deseja continuar? s/n\n')
#     if continuar.upper() == 'S':
#         continue
#     else:
#         break

"""
Calculadora professor
"""
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###
    print('Realizando sua conta. Confira o resultado abaixo')
    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float}=', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float}=', num_1_float * num_2_float)
    else: 
        print('Nunca deveria chegar aqui')

    sair = input('quer sair? [s]im: ').lower().startswith('') # lower retorna tudo minusculo, startswith verifica qual o primeiro caractere
    if sair is True:
        break

    