matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for l in range(0, 5):
    for c in range(0, 5):
        matriz[l][c] = int(input('Digite um número para [{}], [{}] >>> '.format(l, c)))

for l in range(0, 5):
    for c in range(0, 5):
        print('[{:^3}]'.format(matriz[l][c]), end='')
        