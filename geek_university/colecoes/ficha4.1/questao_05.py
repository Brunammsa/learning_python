vetor_1 = []
elementos_pares = []
while True:
    numeros = int(input('Digite 10 números >>> '))
    vetor_1.append(numeros)
    if len(vetor_1) == 10:
        break
for numero_par in vetor_1:
    if numero_par % 2 == 0:
        elementos_pares.append(numero_par)
print('o vetor possui {} elementos pares'.format(len(elementos_pares)))
