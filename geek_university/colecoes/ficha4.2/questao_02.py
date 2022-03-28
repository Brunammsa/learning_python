matriz = [[3, 5, 1, 2, 6], [2, 7, 6, 4, 5], [88, 7, 3, 1, 0], [10, 4, 67, 2, 9], [2, 6, 2, 90, 8]]


for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if linha == coluna:
            matriz[linha][coluna] = 1
        else:
            matriz[linha][coluna] = 0
        print('[{:^3}]'.format(matriz[linha][coluna]), end=' ')
    print()
    