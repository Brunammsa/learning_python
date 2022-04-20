from random import randint

ordem_da_matriz = 5
cartela_de_bingo = []
numero = 1
numeros_que_ja_foram_sorteados = []

# Inicializando uma matriz de ordem 5
for _ in range(ordem_da_matriz):
    linha = []
    for _ in range(ordem_da_matriz):
        linha.append(None)
    cartela_de_bingo.append(linha)

# Inserindo os números aleatórios não repetidos
for i in range(len(cartela_de_bingo)):
    for j in range(len(cartela_de_bingo[i])):
        while numero not in numeros_que_ja_foram_sorteados:
            numero = randint(1, 100)
            if numero not in numeros_que_ja_foram_sorteados:
                numeros_que_ja_foram_sorteados.append(numero)
            else:
                numero = 0
        cartela_de_bingo[i][j] = numero
        numero = 0
print(cartela_de_bingo)

for linha in range(len(cartela_de_bingo)):
    for coluna in range(len(cartela_de_bingo[linha])):
        print('{:^3}'.format(cartela_de_bingo[linha][coluna]), end=' ')
    print()
