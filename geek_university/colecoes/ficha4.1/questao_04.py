vetor_1 = []
resposta = ''
menu = input('Digite 8 números e em seguida escola duas posições para realizar a soma entre elas. Aperte "enter" para começar:\n')

while resposta != 'sair':
    numeros = int(input('Digite 8 números >>> '))
    vetor_1.append(numeros)
    if len(vetor_1) == 8:
        break
pergunta = int(input('Escolha uma posição de 0 a 7 >>> '))
pergunta_2 = int(input('Escolha outra posição diferente da anterior >>> '))
print('A soma da posição {} e da posição {} é igual a {}'.format(pergunta, pergunta_2, vetor_1[pergunta] + vetor_1[pergunta_2]))
