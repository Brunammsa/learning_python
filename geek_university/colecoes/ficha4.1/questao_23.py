vetor_a = [1, 2, 3, 4, 5]
vetor_b = [6, 7, 8, 9, 10]
vetor_escalado = []

for i in range(5):
    vetor_escalado.append(vetor_a[i] * vetor_b[i])
    i += 1

print(vetor_a)
print(vetor_b)
print(sum(vetor_escalado))