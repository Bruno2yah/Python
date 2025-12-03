# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# decoradores são usados para fazer o Python
# usar as funções decoradores em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

# Essa função serve para inverter uma string 
def inverteString(string):
    return string[::-1]

# Verifica se o parametro informado é uma str
def isString(valor):
    if not isinstance(valor, str):
        raise TypeError('O parâmetro informado não é um str')

# Isso é uma função decoradora
def criarFuncao(funcao):
    def interno(string):
        isString(string)
        return inverteString(string)
    return interno

palavra = criarFuncao(inverteString)
print(palavra('Bruno'))
print(palavra('Emily'))