matriz = [
    [1, 7, 0, 4],
    [2, 8, 6, 9],
    [3, 6, 10, 7],
    [4, 5, 10, 8],
    [5, 5, 7, 6]
]

maior_nota_final = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        print('{:^3}'.format(matriz[linha][coluna]), end=' ')
    print()
# a)
aluno = 0
for informacao in matriz:
    aluno = informacao
    print('as três primeiras informações do {} aluno é: {} {} {}'.format(informacao, informacao[0], informacao[1], informacao[2]))
# b)
for nota_final in matriz:
    media_nota_final = (nota_final[1] + nota_final[2]) / 2
    nota_final[3] = media_nota_final
    media_nota_final = 0
print(matriz)
# c)
melhor_nota_final = 0
aluno_melhor_nota_final = 0

for aluno in range(len(matriz)):
    if melhor_nota_final < matriz[aluno][3]:
        melhor_nota_final = matriz[aluno][3]
        aluno_melhor_nota_final = aluno
print('o aluno com a melhor nota final é o {}'.format(aluno_melhor_nota_final))
# d)
soma_notas_finais = 0

for nota_final in matriz:
    soma_notas_finais = soma_notas_finais + nota_final[3]
media_aritimetica_notas_finais = soma_notas_finais / len(matriz)
print('a média aritimética de todas as notas finais é de: {}'.format(media_aritimetica_notas_finais))
