pergunta = int(input('Digite um número: '))
numero = 0

if pergunta < 0 or pergunta %2 == 0:
    print('Número inválido, digite um inteiro positivo e ímpar')
else:
    while pergunta >= numero:
        print(pergunta)
        pergunta -= 2
    print('Fim')