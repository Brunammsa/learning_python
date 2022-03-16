valores = []

while True:
    numeros = int(input('Digite 10 valores >>> '))
    valores.append(numeros)
    if len(valores) == 10:
        break
print('o maior valor digitado foi o {}'.format(max(valores)))
print('o menor valor digitado foi o {}'.format(min(valores)))
