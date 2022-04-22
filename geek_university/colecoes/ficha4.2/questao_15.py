matriz = [
    ['a', 'd', 'd', 'c', 'a', 'e', 'e', 'b', 'a', 'd'],
    ['d', 'c', 'd', 'a', 'a', 'e', 'e', 'd', 'c', 'e'],
    ['e', 'b', 'd', 'a', 'c', 'c', 'e', 'b', 'd', 'e'], 
    ['e', 'e', 'a', 'b', 'd', 'c', 'c', 'e', 'd', 'c'], 
    ['d', 'b', 'd', 'c', 'e', 'a', 'e', 'a', 'c', 'c']
]
n = 0
gabarito = ['a', 'e', 'd', 'c', 'c', 'b', 'a', 'd', 'd', 'a']
resultado = []
soma_da_pontuacao = 0

'''
Extra:

for indice_do_aluno in range(len(matriz)):
    gabarito_aluno = matriz[indice_do_aluno]
    print('Aluno {}:'.format(indice_do_aluno))
    for i in range(len(gabarito_aluno)):
        print('{}) {}'.format(i, gabarito_aluno[i]))
'''

for indice_do_aluno, gabarito_aluno in enumerate(matriz):
    for alternativa in gabarito_aluno:
        if alternativa == gabarito[n]:
            soma_da_pontuacao += 1
        n += 1
    resultado.append(soma_da_pontuacao)
    n = 0
    soma_da_pontuacao = 0
print(resultado)

# Meu jeitinho:

for aluno in range(len(matriz)):
    for questao in range(len(matriz[aluno])):
        if matriz[aluno][questao] == gabarito[questao]:
            soma_da_pontuacao += 1
    resultado.append('aluno {} fez {}'.format(aluno, soma_da_pontuacao))
    soma_da_pontuacao = 0
print(resultado)
