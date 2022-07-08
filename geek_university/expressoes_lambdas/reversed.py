"""
Reversed

OBS.: não confundir com a função reserve() que estudamos em lista, e apenas nela.

- Já a reversed() funciona em qualquer iterável, invertendo-a
- Retorna um iterável chamado List reverse iterator
"""

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)

# Convertendo o elemento retornado para uma lista,  tupla ou conjunto:

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto
print(set(reversed(lista))) # em set não definimos a ordem dos elementos

# Podemos iterar sobre o reverser():

for letra in reversed("\nbruna melo"):
    print(letra, end='')

# Sem o for

print(''.join(list(reversed("bruna melo"))))

# Agora com range

for i in range(9, -1, -1):
    print(i)