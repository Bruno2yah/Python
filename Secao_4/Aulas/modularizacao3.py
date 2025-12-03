# Módulos são singletons, só pode existir 1 no programa
# Para recarregar o módulo é possivel utilizando a biblitoteca "importlib"
# usando a função "reload" com o parametro sendo seu módulo
# ex importlib.reload(módulo)
import importlib

# Por se tratar de singleton, só irá importar uma vez
print(f'range singleton')
for i in range(5): 
    print(i)
    import modularizacao2

# usando esse metodo é possivel recarregar modulos
print('Range com reloaded')
for i in range(5):
    print(i)
    importlib.reload(modularizacao2)
    