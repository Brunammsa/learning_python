from random import randint

matriz_01 = []

for i in range(4):
    numeros_para_a_matriz = randint(1, 20)
    matriz_01.append([numeros_para_a_matriz]*4) # acredito que teria um jeito melhor, mas como preciso atribuir valor 0 p uma parte, deixei assim.

for linha in range(len(matriz_01)):
    for coluna in range(len(matriz_01[linha])):
        print('[{:^3}]'.format(matriz_01[linha][coluna]), end='')
    print()

for i in range(len(matriz_01)):
    for j in range(len(matriz_01[i])):
        if i<j:
            matriz_01[i][j] = 0
        print('[{:^3}]'.format(matriz_01[i][j]), end='')
    print()        
