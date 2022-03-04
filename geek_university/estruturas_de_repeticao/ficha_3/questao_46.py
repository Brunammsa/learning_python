from random import randint

gerador = randint(1, 1000)
print('Adivinhe qual número foi gerado de 1 a 1000\n')

acertou = False

while not acertou:
    adivinhacao = int(input('Qual número você acha que foi gerado >>> '))
    if adivinhacao == gerador:
        acertou = True
        print('\nAcertou!')
    elif adivinhacao < gerador:
        print('\nSeu palpite é menor do que o número gerado')
    else:
        print('\nSeu palpite é maior do que o número gerado')
