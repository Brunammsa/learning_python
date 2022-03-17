vetor = []
multiplos_de_x = []

for i in range(10):
    pergunta = int(input('Digite um valor >>> '))
    vetor.append(pergunta)

x = int(input('Digite um número >>> '))

for numerodovetor in vetor:
    if x % numerodovetor == 0:
        multiplos_de_x.append(numerodovetor)
print('os números {} são multiplos de {}'.format(multiplos_de_x, x))
