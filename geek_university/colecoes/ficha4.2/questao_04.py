matriz = [[3, 5, 1, 2], [2, 2, 6, 4], [2, 1, 3, 1], [2, 4, 1, 2]]
maior_numero = 0
posicao_linha = 0
posicao_coluna = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print('[{:^3}]'.format(matriz[linha][coluna]), end='')
    print()

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] > maior_numero:
            maior_numero = matriz[linha][coluna]
            posicao_linha = linha
            posicao_coluna = coluna
print('a posição do maior valor fica na {},{}'.format(posicao_linha, posicao_coluna))
