matriz_A = [] 

for i in range(10):
    matriz_A.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

for linha in range(len(matriz_A)):
    for coluna in range(len(matriz_A[linha])):
        if linha < coluna:
            matriz_A[linha][coluna] = (2*linha) + (7*coluna)
        elif linha == coluna:
            matriz_A[linha][coluna] = 3*(linha**2) - 1
        elif linha > coluna:
            matriz_A[linha][coluna] = 4*(linha**3) - 5*(coluna**2) + 1

for i in range(len(matriz_A)):
    for j in range(len(matriz_A[i])):
        print('[{:^10}]'.format(matriz_A[i][j]), end='')
    print()
