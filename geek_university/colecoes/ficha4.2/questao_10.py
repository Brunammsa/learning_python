matriz_01 = [[3, 5, 1], [2, 2, 6], [2, 1, 3]]
soma = 0

for linha in range(len(matriz_01)):
    for coluna in range(len(matriz_01[linha])):
        if linha == coluna:
            soma += linha
            soma += coluna
print(soma)
# algo errado tem que dar 7