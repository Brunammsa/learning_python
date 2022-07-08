"""
Zip
- Cria um iterável (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em pares;
"""

# Exemplos:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, "abc")
print(zip1)

# Sempre podemos gerar uma Lista, Tupla e Dict

zip1 = zip(lista1, lista2, "abc")
print(list(zip1))

zip1 = zip(lista1, lista2, "abc")
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

""" OBS.: o zip utilza como parâmetro o menor tamanho em iterável, isso significa que se estiver trabalhando com iteráveis com
tamanhos diferentes, irá parar quando os elementos do menor iterável acabar;"""

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2,lista3)
print(list(zip1))

# OBS.: para descompactar, só usar o *

dados = [(0, 1), (1, 2), (2, 3), (3, 4)]
print(list(zip(*dados)))

# Exemplos mais completox

prova1 = [80, 91, 78]
prova2 = [ 98, 89, 53]
alunos = ["bruno", "bruna", "vanessa"]

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# Utilizando map

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))