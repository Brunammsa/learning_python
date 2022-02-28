pergunta = int(input('Digite um número: '))
numero = 0

if pergunta < 0 or pergunta %2 ==1:
    print('Número inválido, digite um número inteiro, positivo e par')
else:
    while numero <= pergunta:
        print(numero)
        numero +=2
print('Fim')