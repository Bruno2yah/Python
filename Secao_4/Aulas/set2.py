"""
Operadores úteis:
união '|' união (union) - une 
intersecção '&' (intersection) - Itens presentes em ambos
diferença '-' - Itens presentes apenas no set da esquerda
diferença simétrica '^' - Itens que não estão em ambos
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# o operador | serve para unir os dois sets
s3 = s1 | s2
print(f'União {s3} tipo: {type(s3)}')

# o operador & serve para criar um set somente com valores que estão em ambos
s4 = s1 & s2
print(f'Intersecção {s4} tipo: {type(s4)}')

# o operador - serve para criar um set com valores presentes somente na esquerda
s5 = s1 - s2 # ex s1
print(f'Diferença do valor s1: {s5} tipo: {type(s5)}')
s5 = s2 - s1 # ex s2
print(f'Diferença do valor s2: {s5} tipo: {type(s5)}')

# o operador ^ serve para criar um set com valores que não estão em ambos
s6 = s1 ^ s2
print(f'Diferença Simétrica {s6} tipo: {type(s6)}')