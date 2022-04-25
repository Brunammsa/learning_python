matriz = [
    [8, 7, 0],
    [4, 8, 6],
    [8, 6, 10],
    [8, 10, 10],
    [7, 5, 7],
    [10, 8, 9], 
    [3, 5, 7],
    [9, 7, 8],
    [4, 2, 6],
    [7, 5, 8]
]

pior_nota = 0
posicao_pior_nota = 0

alunos_pior_prova = [0, 0, 0]

for aluno in range(len(matriz)):
    pior_nota = matriz[aluno][0]
    posicao_pior_nota = 0
    for posicao_nota in range(len(matriz[aluno])):
        if matriz[aluno][posicao_nota] < pior_nota:
            pior_nota = matriz[aluno][posicao_nota]
            posicao_pior_nota = posicao_nota
    alunos_pior_prova[posicao_pior_nota] = alunos_pior_prova[posicao_pior_nota] + 1

numero_da_prova = 1
for quantidade_de_alunos in alunos_pior_prova:
    print('a quantidade de alunos que se deram mal na prova {} foi {} '.format(numero_da_prova, quantidade_de_alunos))
    numero_da_prova += 1
