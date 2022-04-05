altura_alunos = []
pergunta = []
quantos_alunos = 0

for i in range(10):
    pergunta = float(input('Digite a altura do aluno >>> '))
    altura_alunos.append(pergunta)
    quantos_alunos += 1
print('quantidade de alunos: {}'.format(quantos_alunos))
print(altura_alunos)
print('O aluno mais alto mede {}cm e é o {}º entre todos eles'.format(max(altura_alunos), altura_alunos.index(max(altura_alunos))+1))
print('O aluno mais baixo mede {}cm e é o {}º entre todos eles'.format(min(altura_alunos), altura_alunos.index(min(altura_alunos))+1))
