"""
Ordered Dict

OBS.: a ordem de inserção dos elementos não é garantida
"""

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4}) # com o ordereddict temos a certeza de que estará em ordem

for chave, valor in dicionario.items():
    print('chave: {} valor: {}'.format(chave, valor))