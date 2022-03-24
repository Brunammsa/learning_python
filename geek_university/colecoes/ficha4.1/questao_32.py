vetor_x = [6, 5, 8, 77, 9]
vetor_y = [7, 46, 75, 2, 6]

print(vetor_x)
print(vetor_y)

soma_vetores = []
produto_vetores = []
diferenca_vetores = []
uniao_y_x = []


for index, valor, in enumerate(vetor_x):
    soma_vetores.append(valor + vetor_y[index])
print('a soma de cada index dos vetores x com y é: {}'.format(soma_vetores))

for index, valor in enumerate(vetor_x):
    produto_vetores.append(valor * vetor_y[index])
print('o produto de cada posição dos vetories x com y é: {}'.format(produto_vetores))

x_menos_y = set(vetor_x).difference(set(vetor_y))
print('os elementos de x que não existem em y são {}'.format(list(x_menos_y)))

ambos_vetores = set(vetor_x).intersection(set(vetor_y))
print('a interseção entre os vetores é {}'.format(list(ambos_vetores)))

diferenca_vetores = set(vetor_y).difference(set(vetor_x))
uniao_y_x = set(diferenca_vetores).union(set(vetor_x))
print('a união entre elementos de x com y, com elementos de y que não estão em x é {}'.format(list(uniao_y_x)))