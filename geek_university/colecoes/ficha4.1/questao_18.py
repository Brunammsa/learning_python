vetor = [10, 100, 125, 130, 30, 60, 55, 555, 650, 13]
multiplos_de_x = []
"""
for i in range(10):
    pergunta = int(input('Digite um valor >>> '))
    vetor.append(pergunta)
"""
x = 5

for numero_do_vetor in vetor:
    if numero_do_vetor % x == 0:
        multiplos_de_x.append(numero_do_vetor)
print('os números {} são multiplos de {}'.format(multiplos_de_x, x))
