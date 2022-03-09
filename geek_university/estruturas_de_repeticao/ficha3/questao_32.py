from random import randint

quantidade_lançamento = int(input('Quantas vezes os dados irão ser lançados? >>>  '))

rodada = 0

while rodada < quantidade_lançamento:
    print('Rodada de {}'.format(rodada))
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(d1, d2)
    rodada += 1
    if d1 == d2:
        print( 'D1 deu igual a d2')
    elif d1 < d2:
        print( 'D1 deu menor do que d2')
    else:
        print('D1 deu maior do que d2')   
    