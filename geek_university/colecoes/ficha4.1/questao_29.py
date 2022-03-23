numeros = []
pares = []
impares = []
while len(numeros) < 6:
    numb = int(input('Digite um número >>> '))
    numeros.append(numb)
print('A lista de números gerada foi a {}'.format(numeros))

for index in numeros:
    if index %2 == 0:
        pares.append(index)
    if index %2 != 0:
        impares.append(index)
print('Dentre a lista digitada, os números pares são os {}'.format(pares))
print('A soma dos números pares é {}'.format(sum(pares)))
print('Dentre a lista digitada, os números ímpares são os {}'.format(impares))
print('A quantidade de números ímpares digitados é de {}'.format(len(impares)))

