matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] # usar 0 para não precisar utilizar append
maiores_de_10 = []

for l in range(len(matriz)):
    for c in range(len(matriz)):
        matriz[l][c] = int(input('Digite um número para[{}, {}] >>> '.format(l, c)))
        if matriz[l][c] > 10:
            maiores_de_10.append(matriz[l][c])
print('há {} números maiores do que 10 na matriz abaixo'.format(len(maiores_de_10)))

for l in range(len(matriz)):
    for c in range(len(matriz)):
        print('[{:^3}]'.format(matriz[l][c]), end=' ') # espaçamento de 3 números para não ficar desordenado com números diferentes
    print() # quando acabar o laço, pula linha
