# Fatiamento de Strings
# 012345678
# Olá mundo
#-987654321
# Fatiamento [i:f:p] [::]
# obs.: a função len retorna a quantidade de caracteres da str

variavel = 'Olá mundo'
print(variavel[5])
print(variavel[4:]) #fim omitido
print(variavel[4:7]) #fim declarado
print(len(variavel[0:3]))
print(len(variavel)) # conta a quantidade de str
print(variavel[0:len(variavel)]) 
print(variavel[0:len(variavel):2]) # o passo define a quantidade que vai pular
print(variavel[::-1]) # deixa invertido o texto