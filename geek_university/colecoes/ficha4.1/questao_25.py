vetor = []
numero = 1

while len(vetor) < 100:
    if numero % 7 != 0 or str(numero)[len(str(numero))-1] == str(7):
        vetor.append(numero)
    numero += 1
print(vetor)
