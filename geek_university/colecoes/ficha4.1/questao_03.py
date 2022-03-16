vetor_1 = []
vetor_2 = []

while True:
    numeros = int(input('Digite 10 números >>> '))
    vetor_1.append(numeros)
    if len(vetor_1) == 10:
        break
print(vetor_1)

for elemento in vetor_1:
    vetor_2.append(elemento**2)
print(vetor_2)
