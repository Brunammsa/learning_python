numero = int(input('Digite um número >>> '))

valor = 0

while valor < numero:
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 00:
        print('{} é multiplo de 11, 13 ou 17'.format(numero))
        break
    valor += 1
    