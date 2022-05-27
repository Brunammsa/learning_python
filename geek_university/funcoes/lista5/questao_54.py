matriz = [[3, 5, 8, 0], [7, 2, 6, 1], [2, 1, 3, 5]]

def soma_elementos(matriz_A_4x4):
    soma = 0
    for linha in range(len(matriz_A_4x4)):
        for coluna in range(len(matriz_A_4x4)):
            soma += matriz_A_4x4[linha][coluna]

    return soma

print(soma_elementos(matriz))
#acho que é só isso