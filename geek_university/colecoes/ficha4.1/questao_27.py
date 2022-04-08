vetor = [112, 233, 3123, 554, 75, 16, 17, 318, 39, 5510]
divisores = 0

for i in vetor:
    for j in range(1, i + 1):
        if i % j == 0:
            divisores += 1
    if divisores == 2:
        print('o número {} é primo e sua posição é a {}'.format(j, vetor.index(j)))
    divisores = 0
