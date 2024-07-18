"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro
"""

numero = input('Digite um número inteiro:\n')
if numero.isdigit():
    numero_int = int(numero)
    if (numero_int % 2) == 0:
        print(f'"{numero}" é um número par')
    else:
        print(f'"{numero}" não é um número par')
else:
    print(f'"{numero}" não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, 
exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

hora = input('Digite a hora:(ex: 12)\n')
if hora.isdigit():
    hora_int = int(hora)
    if hora_int <= 11:
        print('Bom dia')
    elif hora_int <= 17:
        print('Boa tarde')
    elif hora_int <= 23:
        print('Boa noite')
    else:
        print('Não existe a hora digitada')
else:
    print('Valor não existe')

"""
Faça um programa que peça o primeiro nome do usuárip. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; 
maior que 6 escreva "seu nome é muito grande"
"""

nome = input('Digite o seu primeiro nome:\n')
if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
else: 
    print('Seu nome é muito grande')
