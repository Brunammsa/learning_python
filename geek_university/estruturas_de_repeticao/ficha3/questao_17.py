pergunta = int(input('Digite um número: '))
soma = 0

if pergunta < 0:
    print('Número inválido, digite um inteiro positivo')
else:
    for i in range(0, pergunta+1):
        soma = soma + i
    print('A soma dos números positivos é {}'.format(soma))
