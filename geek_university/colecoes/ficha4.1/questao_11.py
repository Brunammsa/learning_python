vetor = []
numeros_negativos = []
numeros_positivos = []

for elementos in range(10):
    num = int(input('Digite 10 valores >>> '))
    vetor.append(num)
    if num < 0:
        numeros_negativos.append(num)
    else:
        numeros_positivos.append(num)
print(vetor)
print('a quantidade de valores negativos lidos foi de {}'.format(len(numeros_negativos)))
print('a soma dos valores positivos foi de {}'.format(sum(numeros_positivos)))