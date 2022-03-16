from collections import Counter


valores = []
numeros_repetidos = []

for num in range(20):
    numeros = int(input('Digite 10 valores >>> '))
    valores.append(numeros)
numeros_repetidos = Counter(valores)
print('Os elementos da lista valores sem as repetições fica da seguinte forma:\n{}'.format(numeros_repetidos))
