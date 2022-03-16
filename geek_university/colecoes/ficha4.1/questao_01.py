# a)
vetor_a = [1, 0, 5, -2, -5, 7]

# b)
variavel_soma_a = []

variavel_soma_a.append(vetor_a[0])
variavel_soma_a.append(vetor_a[1])
variavel_soma_a.append(vetor_a[5])
print('a soma dos valores do vetor é de {}'.format(sum(variavel_soma_a)))

# c)
vetor_a.insert(4, 100)
print(vetor_a)

# d)
for elemento in vetor_a:
    print(elemento)