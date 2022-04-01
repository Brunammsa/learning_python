matriz_01 = [[3, 5, 1, 2], [2, 2, 6, 4], [2, 1, 3, 1], [2, 4, 1, 2]]
matriz_02 = [[6, 2, 8, 4], [8, 3, 5, 1], [0, 8, 7, 0], [1, 5, 1, 7]]

maior_posicao_01 = 0
maior_posicao_02 = 0
matriz_03 = []

for linha in range(len(matriz_01)):
    for coluna in range(len(matriz_01[linha])):
        if matriz_01[linha][coluna] > maior_posicao_01:
            maior_posicao_01 = matriz_01[linha][coluna]

for linha in range(len(matriz_02)):
    for coluna in range(len(matriz_02[linha])):
        if matriz_02[linha][coluna] > maior_posicao_02:
            maior_posicao_02 = matriz_02[linha][coluna]

matriz_03.extend([maior_posicao_01, maior_posicao_02])
print(matriz_03)
