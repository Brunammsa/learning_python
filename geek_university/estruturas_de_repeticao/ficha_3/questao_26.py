numero = int(input('Digite um número >>> '))

while True:
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
        print(numero)
        break
    numero += 1
