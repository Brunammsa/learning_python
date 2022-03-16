valores = []

while True:
    numeros = int(input('Digite 6 números inteiros >>> '))
    valores.append(numeros)
    if len(valores) == 6:
        break
valores.reverse()
print('a ordem inversa dos valores digitatos é\n{}'.format(valores))
