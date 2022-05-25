import math

def desvio_padrao(vetor):
    somatoria = 0
    quantidade_elementos_vetor = len(vetor)
    media = sum(vetor)/quantidade_elementos_vetor

    for i in vetor:
        variancia = (i - media) ** 2
        somatoria += variancia

    desvio_padrao_variavel = math.sqrt(somatoria/quantidade_elementos_vetor)
    return desvio_padrao_variavel

print(desvio_padrao([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
