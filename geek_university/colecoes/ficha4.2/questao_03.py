matriz = [[3, 5, 1, 2], [2, 2, 6, 4], [2, 1, 3, 1], [2, 4, 1, 2]]
nova_matriz = []

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        multiplicacao = linha*coluna
        nova_matriz.append(multiplicacao)
    print(nova_matriz)
    nova_matriz = []
