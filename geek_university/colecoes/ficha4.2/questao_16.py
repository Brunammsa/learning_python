gabarito_professor = {
    'questão 1': 'b',
    'questão 2': 'c',
    'questão 3': 'a',
    'questão 4': 'e',
    'questão 5': 'c',
    'questão 6': 'e',
    'questão 7': 'd',
    'questão 8': 'c',
    'questão 9': 'e',
    'questão 10': 'a',
}

pontuacao_aluno = 0
sala_de_aula = [
    {
    'matricula': 12345,
    'nota': 0,
    'gabarito': {
        'questão 1': 'b',
        'questão 2': 'd',
        'questão 3': 'b',
        'questão 4': 'e',
        'questão 5': 'd',
        'questão 6': 'c',
        'questão 7': 'a',
        'questão 8': 'a',
        'questão 9': 'b',
        'questão 10': 'e'
        }
    },{
    'matricula': 67890,
    'nota': 0,
    'gabarito': {
        'questão 1': 'c',
        'questão 2': 'c',
        'questão 3': 'd',
        'questão 4': 'e',
        'questão 5': 'b',
        'questão 6': 'e',
        'questão 7': 'e',
        'questão 8': 'c',
        'questão 9': 'd',
        'questão 10': 'a'
        }
    },{
    'matricula': 54321,
    'nota': 0,
    'gabarito': {
        'questão 1': 'b',
        'questão 2': 'c',
        'questão 3': 'a',
        'questão 4': 'e',
        'questão 5': 'c',
        'questão 6': 'e',
        'questão 7': 'd',
        'questão 8': 'c',
        'questão 9': 'e',
        'questão 10': 'a'
        }
    }
]
passou = 0
for aluno in sala_de_aula:
    pontuacao_aluno = 0
    for questao in gabarito_professor.keys():
        if gabarito_professor[questao] == aluno['gabarito'][questao]:
            pontuacao_aluno += 1
    aluno['nota'] = pontuacao_aluno
    if aluno['nota'] >= 7:
        passou += 1
    print('o aluno {} tirou {}, seu gabarito foi: {}\n'.format(aluno['matricula'], aluno['nota'], aluno['gabarito']))
print('o percentual de aprovação foi {}%'.format(passou / len(sala_de_aula) * 100))
