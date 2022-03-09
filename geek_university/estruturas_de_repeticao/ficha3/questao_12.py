pergunta = int(input('Digite um número: '))
numero = 0

if pergunta < 0:
    print('Número inválido, digite um natural positivo')
else:
    while pergunta >= numero:
        print(pergunta)
        pergunta = pergunta - 1
    print('Fim')
