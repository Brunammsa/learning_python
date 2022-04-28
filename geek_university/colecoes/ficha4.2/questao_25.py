from random import randint


matriz = []
ordem_da_matriz = 3

for _ in range(ordem_da_matriz):
    linha = []
    for _ in range(ordem_da_matriz):
        linha.append(None)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz)):
        numero = randint(-1, 1)
        matriz[i][j] = numero

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print('{:^3}'.format(matriz[linha][coluna]), end=' ')
    print()
