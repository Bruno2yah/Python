nome = 'Bruno'
altura = 1.73
peso = 55
imc = peso / (altura * altura)

linha = 'nome tem altura de altura' # exemplo
# 'f-strings' é chamado de formatação
linha_1 = f'{nome} tem {altura:.4f} de altura' # só de colocar o f inicia formatação, {} coloca variaveis, :.2f defini o tamanho de casas decimais
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2)
print(linha_3)
