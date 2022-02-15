from functools import reduce

def soma(x, y):
    return x+y

lista = [2, 5, 3, 6, 10]

soma = reduce(soma, lista) #aqui ele retorna a soma para x e a lista para y
print(soma)