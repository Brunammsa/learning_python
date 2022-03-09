pergunta = int(input('Digite um número: '))
numero = 0

if pergunta < 0 or pergunta %2 == 1:
    print('Número inválido, digite um inteiro positivo e par')
else:
    while pergunta >= numero:
        print(pergunta)
        pergunta -= 2
    print('Fim')
