n = int(input('Leia um valor inteiro e positivo para "n" >>> '))
E = 1
soma = 0

if n < 0:
    print('Tente novamente')
else:
    while E <= n:
        soma += 1/E
        E += 1
    print('O valor da soma do termo E é igual a {}'.format(soma))
