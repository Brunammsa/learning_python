"""
Map

Com map, fazemso mapeamento de valores para função

"""

import math

def area(r):
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

# Forma comum

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map
# OBS1.: map é uma função que recebe dois parâmetros, o primeiro função, o segundo um iterável

areas = map(area, raios)
print(list(areas))

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS3.: Após a primeira utilização da função map(), ele zera

# Para fixar - Map

"""
- Temos dados iteráveis:
dados: a1, a2, a3...

- Temos uma função:
função: f(x)

Utilizaremos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicas a função

O Map objects: f(a1), f(a2)...

"""

# Mais exemplos

cidades = [('recife', 28), ('aracaju', 30), ('mafra', 5)]

print(cidades)

# lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))