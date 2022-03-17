from random import randint


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares = []

for i in range(0, 50):
    numeros_aleatorios = randint(0, 50)
    numeros.append(numeros_aleatorios)
for numb in numeros:
    if numb % 2 != 0:
        numeros_impares.append(numb)
print(numeros_impares)

for elemento in range(0, len(numeros_impares), 2):
    if elemento + 1 == len(numeros_impares):
        print('{}'.format(numeros_impares[elemento]))
    else:
        print('{} {}'.format(numeros_impares[elemento], numeros_impares[elemento + 1]))
