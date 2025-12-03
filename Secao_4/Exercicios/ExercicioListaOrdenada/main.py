import calculos
import apresentar

# Exercicios 
# Aumente os preços do produto a seguir em 10% 
# Gere novos_produtos por deep copy (copia produnda)

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 2', 'preco': 10.11},
    {'nome': 'produto 3', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]

print('apresentando os produtos tendo aumentado 10%')
novosProdutos = calculos.alterarValorTodosItems(produtos,'preco', 1.10)
apresentar.apresentarLista(novosProdutos)
print('-'*50)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (copia profunda)
print('apresentando os produtos ordenados pelo nome, em ordem decrescente')
produtosOrdenadosNomeDecrescente = calculos.ordenandoLista(produtos, 'nome', True)
apresentar.apresentarLista(produtosOrdenadosNomeDecrescente)
print('-'*50)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia produnda)
print('apresentando os produtos ordenados pelo preço, em ordem crescente')
produtosOrdenadosPreco = calculos.ordenandoLista(produtos, 'preco')
apresentar.apresentarLista(produtosOrdenadosPreco)
print('-'*50)