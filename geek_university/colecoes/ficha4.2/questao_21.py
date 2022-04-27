matriz_01 = [
    [1, 7],
    [2, 8]
]

matriz_02 = [
    [4, 5],
    [5, 3]
]

matriz_03 = [[0,0], [0, 0]]

print('''
~~~~ Menu ~~~~
Escolha uma entre as opções abaixo:

a) Soma as duas matrizes
b) Subtrair a primeira matriz da segunda
c) Adicionar uma constante às duas matrízes
d) Imprimir as duas matrizes
e) sair
''')

opcao_sair = ' '

while opcao_sair != 'sair':
    pergunta = input('digite uma opção >>> ')
    if pergunta == 'a':
        for i in range(len(matriz_01)):
            for j in range(len(matriz_02)):
                soma_matrizes = matriz_01[i][j] + matriz_02[i][j]
                matriz_03[i][j] = soma_matrizes
        print(matriz_03)
    if pergunta == 'b':
        for i in range(len(matriz_01)):
            for j in range(len(matriz_02)):
                soma_matrizes = matriz_01[i][j] - matriz_02[i][j]
                matriz_03[i][j] = soma_matrizes
        print(matriz_03)
    if pergunta == 'c':
        constante = int(input('Digite um número >>> '))
        for i in range(len(matriz_01)):
            for j in range(len(matriz_02)):
                matriz_03[i][j] = constante
        print(matriz_03)
    if pergunta == 'd':
        print(matriz_01)
        print(matriz_02)
        print(matriz_03)
    if pergunta == 'e':
        break