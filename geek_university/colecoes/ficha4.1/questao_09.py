valores = []

while len(valores) <= 5: # 5 porque ele conta com o 0, e sendo assim, fica 6
    numeros = int(input('Digite 6 números pares >>> '))
    if numeros % 2 == 0:
        valores.append(numeros)
valores.reverse()
print('a ordem inversa dos valores pares é\n{}'.format(valores))
