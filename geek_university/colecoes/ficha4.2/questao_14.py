from random import randint

cartela_de_bingo = []
numero = 0

for i in range(5):
    linha1 = randint(1, 99)
    linha2 = randint(1, 99)
    linha3 = randint(1, 99)
    linha4 = randint(1, 99)
    linha5 = randint(1, 99)
    cartela_de_bingo.append([linha1, linha2, linha3, linha4, linha5])    

for linha in range(len(cartela_de_bingo)):
    for coluna in range(len(cartela_de_bingo[linha])):
        if cartela_de_bingo[linha][coluna] in cartela_de_bingo:
            numero += 1
            # quero fazer igual a questão de número primo, mas não to sacando...
            cartela_de_bingo[linha][coluna] = randint(1, 99)
        else:
            print('[{:^3}]'.format(cartela_de_bingo[linha][coluna]), end='')
    print()
