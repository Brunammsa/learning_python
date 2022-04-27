matriz = [
    [1, 7, 0, 4, 15, 8],
    [2, 8, 6, 9, 3, 0],
    [3, 6, 10, 7, 2, 1]
]
# a)
soma = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if coluna % 2 == 0:
            soma = soma + matriz[linha][coluna]
print('a soma de todos os números das colunas ímpares é de {}'.format(soma))
# b)
soma = 0
quantidade_de_valores = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if coluna == 1 or coluna == 3:
            soma = soma + matriz[linha][coluna]
            quantidade_de_valores += 1
media_aritimetica = soma / quantidade_de_valores
print(media_aritimetica)
# c)
soma_da_1e2_coluna = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if coluna == 0 or coluna == 1:
            soma_da_1e2_coluna = soma_da_1e2_coluna + matriz[linha][coluna]

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if coluna == 5:
            matriz[linha][coluna] = soma_da_1e2_coluna
print(matriz)
# d)
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print('{:^3}'.format(matriz[linha][coluna]), end=' ')
    print()