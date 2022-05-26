
matriz_teste = [[3, 5, 11, 2], [67, 2, 6, 4], [2, 1, 3, 34], [2, 4, 1, 2]]

def maior_valor(matriz):
    num_aux = 10
    valores_maiores_do_que_10 = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):

            if matriz[linha][coluna] > num_aux:
                valores_maiores_do_que_10 += 1

    return valores_maiores_do_que_10


print(maior_valor(matriz_teste))
