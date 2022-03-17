vetor = []

for i in range(50):
    calculo = (i + 5 * i) % (i + 1)
    vetor.append(calculo)
print(vetor)
print(len(vetor))