# Módulos padrão do Python (import, from, as e *)
# Pode utilizar a forma que preferir, não deixa o programa mais pesado, ou mais leve
# https://docs.python.org/3/py-modindex.html


# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes0

import sys 

platform = 'A minha'
print(sys.platform) # sempre que utilizar o modulo precisa escrever completo
print(platform)

# Partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: sem o namespace do módulo

from pandas import Categorical, cut

# Dessa forma teria acesso a essas funções e classes, sem ter que ficar digitando o nome do modulo
# Mas tem que se atentar, porque se definir outra variavel com o mesmo nome, perde acesso a elas

# alias 1 - import nomeModulo as apelido
import sys as s 
print(s.platform)

# alias 2 - from nome
from sys import platform as pf, exit as ex 
print(pf)

# Vatagens:  você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# Má prática - from nomeModulo import *
# Vantagem : importa tudo de um módulo
# Desvantagens: importa tudo de um módulo