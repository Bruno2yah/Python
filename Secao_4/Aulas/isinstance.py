# isinstance - para saber se objeto é de determinado tipo

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0,1}, {'nome': 'luiz'},
]

for item in lista: 
    if isinstance(item, set): # irá reproduzir apenas se o valor for set
        print('SET')
        item.add(5)
        print(item, isinstance(item, set)) # irá mostrar se é tipo set
    if isinstance(item, str):
        print(f'String\n{item.upper()}')
    if isinstance(item, (int, float)):
        print(f'NUM\n{item*2}')
    