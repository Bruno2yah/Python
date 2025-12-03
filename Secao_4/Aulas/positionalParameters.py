"""
Controlando a quantidade de argumentos posicionais e nomeados em funções
*args (ilimitado de argumentos posicionais)
**kwargs (ilimidade de argumentos nomeados)
Positional-only Parameters (/) = tudu antes da barra dever ser APENAS posicional.
PEP 570 - Python Positional-Only Parameters
https://peps.python.org/pep-0570/
keyword-Only Arguments (*) - * sozinho NÃO SUGA valores
PEP 3102 - Keyword-Only Arguments
https://peps.python.org/pep-3102/
"""

def soma(*args):
    print(sum(args) )

# o que vem antes da / não pode ser usado como nomeado
def soma(x, y, /):
    print(x + y)

# tudo que vai depois do * é nomeado e não posicional
def subtrair(*, x, y):
    print(x - y)

subtrair(y=4, x=3)
