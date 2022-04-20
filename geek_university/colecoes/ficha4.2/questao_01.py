matriz = []
maiores_de_10 = []
ordem_matriz = 4

# Inicializando a matriz de ordem 4
for _ in range(ordem_matriz):
    linha = []
    for _ in range(ordem_matriz):
        linha.append(0)
    matriz.append(linha)

for l in range(len(matriz)):
    for c in range(len(matriz)):
        matriz[l][c] = int(input('Digite um número para[{}, {}] >>> '.format(l, c)))
        if matriz[l][c] > 10:
            maiores_de_10.append(matriz[l][c])
print('há {} números maiores do que 10 na matriz abaixo'.format(len(maiores_de_10)))

for l in range(len(matriz)):
    for c in range(len(matriz)):
        print('{:^3}'.format(matriz[l][c]), end=' ') # espaçamento de 3 números para não ficar desordenado com números diferentes
    print() # quando acabar o laço, pula linha
