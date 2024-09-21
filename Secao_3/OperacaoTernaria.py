"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# variavel = 'valor' if condicao else 'Outro valor'
# print(variavel)

digito = 10
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

# print('valor' if True else 'outro valor' if True else 'Fim')