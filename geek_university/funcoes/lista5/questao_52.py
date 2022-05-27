
matriz_teste = [[2, 5, 8], [6, 1, 3], [4, 7, 10]]

def quadrado_da_matriz(matriz):
    matriz_quadrada_transposta = []
    ordem_da_matriz = 3

    for _ in range(ordem_da_matriz):
        linha = []
        for _ in range(ordem_da_matriz):
            linha.append(None)
        matriz_quadrada_transposta.append(linha)

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            quadrado = matriz[linha][coluna] ** 2
            matriz_quadrada_transposta[coluna][linha] = quadrado
    
    print(matriz_quadrada_transposta)


quadrado_da_matriz(matriz_teste)
