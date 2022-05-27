matriz_quadrada_A = [[9, 16, 4], [25, 4, 1], [1, 36, 9]]
matriz_quadrada_B = [[4, 36, 16], [25, 1, 49], [64, 9, 100]]
matriz_c = [[None, None, None], [None, None, None], [None, None, None]]

def produto_matricial(matriz_a, matriz_b, matriz_c):

    for linha in range(len(matriz_a)):
        for coluna in range(len(matriz_a[linha])):
            matriz_c[linha][coluna] = matriz_a[linha][coluna] * matriz_b[linha][coluna]
            
    return matriz_c


print(produto_matricial(matriz_quadrada_A, matriz_quadrada_B, matriz_c))