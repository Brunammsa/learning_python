vetor = []

for elementos in range(5):
    numeros = int(input('Digite 10 números reais >>> '))
    vetor.append(numeros)

for index, valor in enumerate(vetor): # index é a posição, quer dizer, e o valor é o valor que encontra-se no index correspondente
    if valor < 0: # como só modificaremos os valores negativos, então usaremos só o valor
        vetor[index] = 0 # e se acima o valor for negativo, então o valor do index mudará para 0
print(vetor)