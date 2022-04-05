valores = []
numeros_repetidos = []

for num in range(20):
    numeros = int(input('Digite 20 valores >>> '))
    valores.append(numeros)
print('Os elementos da lista valores sem as repetições fica da seguinte forma:\n{}'.format(set(numeros_repetidos)))
