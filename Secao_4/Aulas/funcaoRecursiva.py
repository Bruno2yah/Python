"""
Funções recursivas e recursividade
 - Funções que podem se chamar de volta
 - úteis p/ dividir problemas grandes em partes menores
 Toda função recursiva deve ter:
 - um problema que possa ser dividido em partes menores
 - um caso recursivo que resolve o pequeno problema
 - um caso base que para a recursao
 - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

 https://brasilescola.uol.com.br/matematica/fatorial.htm
"""

def recursiva(inicio=0, fim=4):
    # Caso base 
    if inicio >= fim:
        return fim
    
    print(inicio, fim)

    # Caso recursivo
    # Contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

# fatorial

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n -1)

print(factorial(5))
print(factorial(52))