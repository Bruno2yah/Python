# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opções': ['1', '3', '4', '5'],
        'resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5x5?',
        'opções': ['25', '55', '10', '51'],
        'resposta': '25',
    },
    {
        'pergunta': 'Quanto é 10/2?',
        'opções': ['4', '5', '2', '1'],
        'resposta': '5',
    }
]

acertos = 0

opcoesFormatadas = ['a', 'b', 'c', 'd']

for pergunta in perguntas:
    print(f'{pergunta['pergunta']}')
    while True:
        i = 0
        for opcao in pergunta['opções']:
            print(f'{opcoesFormatadas[i]}) {opcao}')
            if opcao == pergunta['resposta']:
                opcaoCorreta = pergunta['opções'].index(opcao)
            i += 1

        resposta = input('Escolha uma opção: ')
        if resposta == 'a' or resposta == 'A':
            resposta = 0
        elif resposta == 'b' or resposta == 'B':
            resposta = 1
        elif resposta == 'c' or resposta == 'C':
            resposta = 2
        elif resposta == 'd' or resposta == 'D':
            resposta = 3
        else:
            print('\nValor inválido, por favor digite um dos valores: a/b/c/d')
            continue

        if resposta == opcaoCorreta:
            acertos += 1
            print('Você acertou! 👍\n')
            break
        else:
            print('Você errou! ❌\n')
            break

print(f'Você acertou {acertos}\nde {len(perguntas)} perguntas.')