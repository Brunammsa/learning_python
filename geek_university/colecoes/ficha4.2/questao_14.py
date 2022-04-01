from random import randint

cartela_de_bingo = []
valor_repetido = 1

for i in range(5):
    linha1 = randint(1, 99)
    linha2 = randint(1, 99)
    linha3 = randint(1, 99)
    linha4 = randint(1, 99)
    linha5 = randint(1, 99)
    cartela_de_bingo.append([linha1, linha2, linha3, linha4, linha5])    

for linha in range(len(cartela_de_bingo)):
    for coluna in range(len(cartela_de_bingo[linha])):
        print('[{:^3}]'.format(cartela_de_bingo[linha][coluna]), end='')
    print()

# agora preciso percorrer cada valor pegar os repetidos e mudar