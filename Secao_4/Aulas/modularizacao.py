# Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se  __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas 
# abaixo dele 
# Ele não reconhece pastas e módulos acima do __main__ port
# padrão
# O python conhece todos os módulos e pacotes presentes 
# nos caminhos de sys.path

# dessa forma você consegue importar seus modulos
import modularizacao2

# Vale ressaltar de não utilizar nomes de módulos feitos, porque daria errado para importar bibliotecas
# Ex: criar um arquivo chamado "Pandas"

print('Este módulo se chama', __name__)

# utilizando atributos e metodos

print(modularizacao2.nome)
print(modularizacao2.soma(2,4))