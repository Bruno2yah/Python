
"""
Introdução ao desempacotamento + tuplas (tuplas)
"""
import os 
os.system('cls')
# nomes = ['Maria', 'Emily', 'Bruno']
# nome1, nome2, nome3 = nomes 
nome1, *_ = ['Maria', 'Emily', 'Bruno'] # *criar variavel de resto
print(nome1)