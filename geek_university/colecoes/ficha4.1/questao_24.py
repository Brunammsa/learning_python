altura_alunos = []
pergunta = []

for i in range(5):
    pergunta = float(input('Digite a altura do aluno >>> '))
    altura_alunos.append(pergunta)

print(altura_alunos)
print('O aluno mais alto mede {}cm e é o {}º entre todos eles'.format(max(altura_alunos), altura_alunos.index(max(altura_alunos))+1))
print('O aluno mais baixo mede {}cm e é o {}º entre todos eles'.format(min(altura_alunos), altura_alunos.index(min(altura_alunos))+1))
