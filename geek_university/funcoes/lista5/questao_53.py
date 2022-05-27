matriz_teste_1 = [[3, 5, 11], [67, 2, 6], [2, 1, 3]]
matriz_quadrada = [[9, 4489, 4], [25, 4, 1], [121, 36, 9]]

matriz_teste_2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def matriz_identidade(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False

    return True

print(matriz_identidade(matriz_teste_1))
print(matriz_identidade(matriz_quadrada))
print(matriz_identidade(matriz_teste_2))

