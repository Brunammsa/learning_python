dividendo = int(input('Digite um número dividendo >>> '))
soma_divisores = 0
divisor = 1

while divisor < dividendo:
    divisao = dividendo % divisor
    if divisao == 0:
        print(divisor)
        soma_divisores += divisor
    divisor += 1
print('A soma dos dividores é {}'.format(soma_divisores))