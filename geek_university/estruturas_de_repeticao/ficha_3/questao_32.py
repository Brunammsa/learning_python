from random import randint

quantidade_lancamentos = int(input('Quantas vezes o dado irá ser lançado? >>> '))

rodada = 1

while rodada <= quantidade_lancamentos:
    print('Rodada de nº {}'.format(rodada))
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(d1, d2)
    if d1 == d2:
        print('D1 deu igual ao d2')
    elif d1 > d2:
        print( 'D1 deu maior do que o d2')
    else:
        print('D1 deu menor do que o d2')
    rodada += 1
