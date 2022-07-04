"""
Generators Expression ou Tuple Comprehension.

nomes = ['bruna', 'bruno', 'breno', brenand', 'luquinhas']

print(any([nome[0] == 'l' for nome in nomes]))

"""

# Poderíamos ter utilizado Generators
nomes = ['bruna', 'bruno', 'breno', 'brenand', 'luquinhas']

print(any(nome[0] == 'l' for nome in nomes)) # a única diferença com o list comprehension é que não tem o []

from sys import getsizeof # retorna a quantidade de bytes em memória do elemento passado em parâmetro "pega o tamanho de"

print(getsizeof('bruna'))

print(getsizeof(5))

print(getsizeof(145334456677755))

# Gerando uma lista de números com List Comprehension

list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension

set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dict Comprehension

dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generators

generators = getsizeof(x * 10 for x in range(1000))

print(f'list: {list_comp} bytes')
print(f'set: {set_comp} bytes')
print(f'dict: {dict_comp} bytes')
print(f'generators: {generators} bytes')

# Será que posso iterar no Generators?

gen = (x * 10 for x in range(100))

for num in gen:
    print(num)
