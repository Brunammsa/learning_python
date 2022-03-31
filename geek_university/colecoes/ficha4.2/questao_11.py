matriz_01 = [[3, 5, 1], [2, 2, 6], [2, 1, 3]]
soma = 0

for linha in range(len(matriz_01)):
    for coluna in range(len(matriz_01[linha])):
        if matriz_01[linha][coluna] == 3:
            soma += matriz_01[linha][coluna]
print(soma)
# deveria dar 5