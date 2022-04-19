vetor = []
tamanho_triangulo = 6
vetor_anterior = []

for j in range(tamanho_triangulo):
    for i in range(j + 1):
        if j == i or i == 0:
            vetor.append(1)
        else:
            vetor.append(vetor_anterior[i] + vetor_anterior[i-1])
    print(vetor)
    vetor_anterior = vetor
    vetor = []
