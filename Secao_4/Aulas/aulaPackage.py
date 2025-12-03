import sys

# Existem essas formas
# Essa importa o modulo inteiro, porém tem que digitar a pasta junto
import introducaoPackage.modulo
# Essa importa o modulo inteiro
from introducaoPackage import modulo
# Essa forma importa somente as funções
from introducaoPackage.modulo import soma

# irá reproduzir tudo que está no __init__ quando o pacote for chamado


print(introducaoPackage.modulo.soma(1, 2))
print(modulo.soma(1, 2))
print(soma(1, 2))