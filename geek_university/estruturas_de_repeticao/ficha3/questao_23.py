'''numero = int(input('Digite um número >>> '))

if numero < 0:
    print('Tente com um número positivo')
else:
    for dividor in range(1, numero+1):
        if numero % dividor == 0:
            print(dividor)
'''
numero = int(input('Digite um número >>> '))
valor = 1

while valor <= numero:
    divisao = numero % valor
    if divisao == 0:
        print(valor)
    valor += 1