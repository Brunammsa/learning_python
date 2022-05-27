matriz_teste = [[3, 5, 11], [67, 2, 6], [2, 1, 3]]

def soma_diagonal_principal_secundaria(matriz):

    soma_principal = 0
    soma_secundaria = 0
    aux_secundaria = 2

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):

            if linha == coluna:
                soma_principal += matriz[linha][coluna]
            if linha + coluna == aux_secundaria:
                soma_secundaria += matriz[linha][coluna]

    return soma_principal, soma_secundaria


print(soma_diagonal_principal_secundaria(matriz_teste))