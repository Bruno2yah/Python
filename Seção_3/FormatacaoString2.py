# Formatação básica de strings 
# s - string
# d - int
# f - float
# .<numero de digitos>f
# (caractere) (><^) (quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - Força o numero a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100, .1f
# Conversion flags - !r !s !a

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}') #coloca 10 caracteres à esquerda
print(f'{variavel: <10}') #coloca 10 caracteres à direita
print(f'{variavel:+^10}') #coloca 10 caracteres no ao redor
print(f'{1000.89421646634729833:.1f}')
print(f'{1000.89421646634729833:,.1f}') #usando , para separar o milhar
print(f'{1000.89421646634729833:+,.1f}')
print(f'{1000.89421646634729833:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')