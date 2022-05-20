import math

def desvio_padrao(vetor):
    somatoria = 0
    quantidade_vetor = 0
    media = sum(vetor)/quantidade_vetor

    for i in vetor:
        variancia = (i - media) ** 2
        somatoria += variancia
        quantidade_vetor += 1

    desvio_padrao_variavel = math.sqrt(somatoria*1/quantidade_vetor-1)
    return desvio_padrao_variavel

print(desvio_padrao([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# não to conseguindo