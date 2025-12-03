"""
ITERÁVEL - > STR, RANGE, ETC (__iter__)
Iterador - > quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter - > me entregue seu iterador
"""

texto = 'Bruno'.__iter__()
print(texto)


texto = iter('Bruno')
print(texto)

texto = iter('Bruno')
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
#quando esgota os valores um error é levantado

texto = iter('Bruno')
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

# for letra in texto
texto = 'Bruno' # iterável
iterador = iter(texto) # iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
