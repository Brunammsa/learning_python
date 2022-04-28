from random import randint


matriz_A = []
matriz_B = []
ordem_da_matriz = 3

for _ in range(ordem_da_matriz):
    linha = []
    for _ in range(ordem_da_matriz):
        linha.append(None)
    matriz_A.append(linha)
    matriz_B.append(linha)

for i in range(len(matriz_A)):
    for j in range(len(matriz_A)):
        numero = randint(1, 10)
        matriz_A[i][j] = numero
print(matriz_A)

for linha in range(len(matriz_A)):
    for coluna in range(len(matriz_A)):
        quadrado = matriz_A[linha][coluna] ** 2
        matriz_B[linha][coluna] = quadrado
print(matriz_B)