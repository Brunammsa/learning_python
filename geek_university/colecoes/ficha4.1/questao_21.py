from random import randint

vetor_a = []
vetor_b = []
vetor_c = []

for i in range(10):
    elementos_dentro_de_A = randint(0,10)
    vetor_a.append(elementos_dentro_de_A)
    elementos_dentro_de_B = randint(0,10)
    vetor_b.append(elementos_dentro_de_B)
print(vetor_a)
print(vetor_b)

# forma 1
for numb_a, numb_b in enumerate(vetor_a):
    vetor_c.append(numb_b - vetor_b[numb_a])
print('{}\n'.format(vetor_c))

# forma 2
zip(vetor_a, vetor_b) # mesclando dois iteráveis
for numb_a, numb_b in zip(vetor_a, vetor_b):
    vetor_c.append(numb_a - numb_b)
print(vetor_c)
