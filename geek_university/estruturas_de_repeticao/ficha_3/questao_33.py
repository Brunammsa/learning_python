n = int(input('Leia um valor inteiro e positivo para "n" >>> '))
i = int(input('Leia um valor inteiro e positivo para "i" >>> '))
j = int(input('Leia um valor inteiro e positivo para "j" >>> '))

valor = 1

if n < 0 or i < 0 or j < 0:
    print('Valores inválidos, tente novamente')
else:
    while valor < n:
        multiplicacao = n * valor
        if multiplicacao % i == 0:
            ...
        if multiplicacao % j == 0:
            ...

# Preciso de ajuda