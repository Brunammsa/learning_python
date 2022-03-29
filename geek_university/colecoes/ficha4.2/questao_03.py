matriz = [[3, 5, 1, 2], [2, 2, 6, 4], [2, 1, 3, 1], [2, 4, 1, 2]]
nova_matriz = []
multi = 1


for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if linha == 0 and coluna <= 3:
            multi *= matriz[linha]
            multi *= coluna
        nova_matriz.append([multi])
multi = 1
print(nova_matriz)

# cotninuar tentando