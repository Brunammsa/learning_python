matriz_A = [[3, 5, 1], [2, 2, 6], [2, 1, 3]]

for linha in range(len(matriz_A)):
    for coluna in range(len(matriz_A[linha])):
        print('[{:^3}]'.format(matriz_A[coluna][linha]), end='')
    print()
