vetor = [112, 233, 3123, 554, 75, 16, 17, 318, 17, 5510]
divisores = 0

"""
****** Com for ******
for index, valor in enumerate(vetor):
    for j in range(1, valor + 1):
        if valor % j == 0:
            divisores += 1
    if divisores == 2:
        print('o número {} é primo e sua posição é a {}'.format(j, index))
    divisores = 0
"""
# ***** Com while *****

index = 0

while index < len(vetor):
    valor = vetor[index]
    for j in range(1, valor + 1):
        if valor % j == 0:
            divisores += 1
    if divisores == 2:
        print('o número {} é primo e sua posição é a {}'.format(j, index))
    divisores = 0
    index += 1
