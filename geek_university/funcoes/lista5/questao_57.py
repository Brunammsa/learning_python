matriz_teste = [[1, 2, 3, 4, 5, 6], [7, 6, 5, 4, 3, 2], [0, 9, 8, 7, 6, 5], [1, 2, 3, 4, 5, 6], [7, 6, 5, 4, 3, 2], [0, 9, 8, 7, 6, 5], [7, 6, 5, 4, 3, 2]]

def soma_linha(matriz, n_da_coluna):
    soma = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if coluna == n_da_coluna:
                soma += matriz[linha][coluna]
    
    return soma


print(soma_linha(matriz_teste, 5))