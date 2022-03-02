'''
Número harmônico:
H(n) = 1 + 1/2 + 1/3 + 1/4 + ... 1/n
'''

n = int(input('Leia um valor inteiro e positivo para "n" >>> '))

valor = 1
soma = 0

if n < 0:
    print('Tente novamente')
else:
    while valor <= n:
        soma += + 1/valor
        valor += 1
    print('A soma da série Harmônica é de {}'.format(soma))
