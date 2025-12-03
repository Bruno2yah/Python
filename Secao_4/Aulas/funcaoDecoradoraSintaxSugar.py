# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# decoradores são usados para fazer o Python
# usar as funções decoradores em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)


# Verifica se o parametro informado é uma str

# Isso é uma função decoradora
def criarFuncao(funcao):
    def interno(string):
        isString(string)
        resultado = funcao(string)
        return resultado
    return interno

# Essa função serve para inverter uma string 
@criarFuncao # usando essa linha de codigo, já faz o python utilizar criarFunção nessa function
def inverteString(string):
    return string[::-1]

def isString(valor):
    if not isinstance(valor, str):
        raise TypeError('O parâmetro informado não é um str')
        
palavraInvertida = inverteString('Bruno')
print(palavraInvertida)
