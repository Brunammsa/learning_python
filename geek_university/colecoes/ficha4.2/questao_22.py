from random import randint


ordem_das_matrizes = 3
matriz_01 = []
matriz_02 = []
matriz_03 = []
numero_matriz01 = 1
numero_matriz02 = 1

for _ in range(ordem_das_matrizes):
    linha = []
    for _ in range(ordem_das_matrizes):
        linha.append(None)
    matriz_01.append(linha)
    matriz_02.append(linha)
    matriz_03.append(linha)

for i in range(len(matriz_01)):
    for j in range(len(matriz_01[i])):
        numero_matriz01 = randint(1, 10)
        matriz_01[i][j] = numero_matriz01
print(matriz_01)

for i in range(len(matriz_02)):
    for j in range((len(matriz_02[i]))):
        numero_matriz02 = randint(1, 10)
        matriz_02[i][j] = numero_matriz02
print(matriz_02)

for linha in range(len(matriz_01)):
    for coluna in range(len(matriz_02)):
        multiplicacao = matriz_01[linha][coluna] * matriz_02[linha][coluna]
        matriz_03[linha][coluna] = multiplicacao   
print(matriz_03)
