notas = []
soma_das_notas = 0

for nota in range(15):
    notas_alunos = float(input('Digite a nota de 15 alunos >>> '))
    notas.append(notas_alunos)
    soma_das_notas += notas_alunos
print(notas)
print('a média geral das notas dos 15 alunos é de {}'.format(round(soma_das_notas/15,2)))

