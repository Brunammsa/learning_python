while True:
    numero = int(input('Digite um número natural: '))
    if numero == 0:
        par = numero
        impar = numero
    if numero % 2 == 0:
        par = numero
        print('O número {} é par'.format(par))
    elif numero % 2 == 1:
        impar = numero
        print('O número {} é impar'.format(impar))
