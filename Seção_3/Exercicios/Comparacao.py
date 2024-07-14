primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if(int(primeiro_valor) > int(segundo_valor)):
    print(f'{primeiro_valor=} é maior do que o {segundo_valor=}')
elif(int(primeiro_valor) == int(segundo_valor)):
    print(f'{primeiro_valor=} é igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior do que o {primeiro_valor=}')
