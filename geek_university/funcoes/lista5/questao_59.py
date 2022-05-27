vetor_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor_B = [11, 2, 13, 14, 15, 6, 17, 10, 7, 20]
vetor_uniao_A_com_B = []

def uniao_vetores(vetor1, vetor2, vetor_uniao):

    for elemento in range(10):
        vetor_uniao_A_com_B = vetor_A + vetor_B
    
    return vetor_uniao_A_com_B


print(uniao_vetores(vetor_A, vetor_B, vetor_uniao_A_com_B))