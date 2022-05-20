def elementos_impares_pares(vetor_x):
    vetor_A = []
    vetor_B = []
    for i in vetor_x:
        if i %2 == 0:
            vetor_A.append(i)
        else:
            vetor_B.append(i)
    return vetor_A, vetor_B

print(elementos_impares_pares([1, 2, 3, 4, 5]))