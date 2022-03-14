"""
Named Tuple: são tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros

"""
# Relembrando

tupla = [1, 2, 3]
print(tupla[1])

# Importando

from collections import namedtuple

# É necessário definir nome e parâmetro
# Forma 1 // declaração namedtuple

gatos = namedtuple('gato', 'idade raça nome') # uma str só separada por " "

# Forma 2

gatos = namedtuple('gato', 'idade, raça, nome') # uma str só separada por ","

# Forma 3

gatos = namedtuple('gato', ['idade', 'raça', 'nome']) # strs diferentes

haru = gatos(idade=9, raça='SRD', nome='Haru')
print(haru)

# Acessando dados // forma 1

print(haru[0])
print(haru[1])
print(haru[2])

# forma 2

print(haru.idade)
print(haru.raça)
print(haru.nome)

print(haru.index('SRD')) # qual a posição do index determinado
print(haru.count('SRD'))
    