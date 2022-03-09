pergunta = int(input('Digite um número: '))
numero = 1

if pergunta < 0 or pergunta %2 == 0:
    print('Número inválido, digite um inteiro positivo e ímpar')
else:
    while numero <= pergunta:
        print(numero)
        numero += 2
    print('Fim')