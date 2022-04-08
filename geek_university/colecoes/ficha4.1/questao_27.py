vetor =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
divisores = 0

for i in vetor:
    for j in range(1, i + 1):
        if i % j == 0:
            divisores += 1
    if divisores == 2:
        print('o número {} é primo e sua posição é a {}'.format(j, i))
    divisores = 0
