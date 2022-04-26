tamanho_da_matriz = 3
matriz = []
array_unidimensional = []
soma = 0

for _ in range(tamanho_da_matriz):
    linha = []
    for _ in range(tamanho_da_matriz):
        linha.append(None)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        numero = int(input('Digite um número >>> '))
        matriz[i][j] = numero

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print('{:3^}'.format(matriz[linha][coluna]), end=' ')
    print()

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        soma = soma + matriz[c][l]
    array_unidimensional.append(soma)
    soma = 0
print(array_unidimensional)