
matriz_teste = [[3, 5, 11], [67, 2, 6], [2, 1, 3]]

def soma_diagonal_principal(matriz):
    soma = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if linha == coluna:
                soma += matriz[linha][coluna]
    return soma

print(soma_diagonal_principal(matriz_teste))