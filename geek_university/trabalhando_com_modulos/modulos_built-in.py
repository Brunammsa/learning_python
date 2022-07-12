"""
Módulos built-in são aqueles que já vêm integrado ao python.
"""

# Utilizando alias (apelidos) para módulos/funções
# Exemplo 1:
import random as rdm

print(rdm.random())

# Exemplo 2:
from random import randint as rdt

print(rdt(2, 4))

# Podemos importar todas as funções de um módulo utilizando o *

from random import * # para mim este não faz sentido

print(random())

# Para múltiplos imports, costumamos utilizas tuplas

from random import{
    random,
    randint,
    choice,
    shuffle
}
