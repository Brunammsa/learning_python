from random import randint


vetor = []
vetor_compactado = []

while len(vetor) < 15:
    numb = randint(0, 15)
    vetor.append(numb)
print(vetor)

for i in vetor:
    if i != 0:
        vetor_compactado.append(i)
print(vetor_compactado)
