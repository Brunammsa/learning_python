matriz_01 = [[3, 5, 1], [2, 2, 6], [2, 1, 3]]
soma = 0

for linha in range(len(matriz_01)):
    for coluna in range(len(matriz_01[linha])):
        print('[{:^3}]'.format(matriz_01[linha][coluna]), end=' ')
        if linha == coluna:
            soma += matriz_01[linha][coluna]
    print()
print(soma)
