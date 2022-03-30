matriz = [[3, 5, 1, 2, 6], [2, 7, 6, 4, 5], [88, 7, 3, 1, 0], [10, 4, 67, 2, 9], [2, 6, 2, 90, 8]]
x = 5
posicao_linha = 0
posicao_coluna = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if matriz[linha][coluna] == x:
            posicao_linha = linha
            posicao_coluna = coluna
            print('achei e a posição é a {},{}'.format(posicao_linha, posicao_coluna))
"""        else:
            print('não achei')"""
# ta certo, mas ta printando demais, fica melhor sem printar o else
