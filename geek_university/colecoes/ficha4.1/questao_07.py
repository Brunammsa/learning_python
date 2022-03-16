vetor = []

while True:
    numero = int(input('Digite 10 números >>> '))
    vetor.append(numero)
    if len(vetor) == 10:
        break
print(vetor)
print('o maior valor do vetor é o {}'.format(max(vetor)))
print('a posição do maior maior valor do vetor é {}'.format(vetor.index(max(vetor))))
