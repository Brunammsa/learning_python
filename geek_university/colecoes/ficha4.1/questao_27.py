vetor = []
divisores = 0

for i in range(10):
    numb = int(input("Digite um número para armazena-lo:"))
    vetor.append(numb)
    for j in range(1, numb):
        if numb % j == 0:
            divisores += 1
    if divisores > 2:
        print('{} não é primo'.format(j))
    else:
        for index, valor in enumerate(vetor):    
            print('{} é primo na posição {}'.format(valor, index))

# ainda não to acertandoooooooooooooo