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

alunos_pior_prova1 = 0
alunos_pior_prova2 = 0
alunos_pior_prova3 = 0

for aluno in range(len(matriz)):
    pior_nota = matriz[aluno][0]
    posicao_pior_nota = 0
    for nota in range(len(matriz[aluno])):
        if matriz[aluno][nota] < pior_nota:
            pior_nota = matriz[aluno][nota]
            posicao_pior_nota = nota
    if posicao_pior_nota == 0:
        alunos_pior_prova1 += 1
    elif posicao_pior_nota == 1:
        alunos_pior_prova2 += 1
    else:
        alunos_pior_prova3 += 1
print('a quantidade de alunos que se deram mal na prova {} foi {} '.format(1, alunos_pior_prova1))
print('a quantidade de alunos que se deram mal na prova {} foi {} '.format(2, alunos_pior_prova2))
print('a quantidade de alunos que se deram mal na prova {} foi {} '.format(3, alunos_pior_prova3))
