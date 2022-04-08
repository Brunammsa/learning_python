import math

vetor_v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somatoria = 0
media_vetor = sum(vetor_v)/len(vetor_v)

for i in vetor_v:
    variancia = (i - media_vetor) ** 2
    somatoria += variancia

desvio_padrao = math.sqrt(somatoria * 1/len(vetor_v)-1)
print(desvio_padrao)
