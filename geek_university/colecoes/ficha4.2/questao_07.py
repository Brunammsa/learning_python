matriz_A = [[3, 5, 1, 2], [2, 2, 6, 4], [2, 1, 3, 1], [2, 4, 1, 2]] # a questão pede 10x10 mas vai ficar grande demais

for linha in range(len(matriz_A)):
    for coluna in range(len(matriz_A[linha])):
        if linha < coluna:
            matriz_A[linha][coluna] = (2*linha) + (7*coluna)
        elif linha == coluna:
            matriz_A[linha][coluna] = 3*(linha**2) - 1
        elif linha > coluna:
            matriz_A[linha][coluna] = 4*(linha**3) - 5*(coluna**2)
# não entendi qual o resultado que a questão pede