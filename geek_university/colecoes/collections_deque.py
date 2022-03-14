"""
Deque: pode-se dizer ser uma lista de alta performace
"""
from collections import deque

# Criando deques

deq = deque('Bruna') #slipitou a str transformando em lista
print(deq)

# Adicionando elementos

deq.append(' M') # adc ao final da lista
print(deq)

deq.appendleft('M, ') # adc no começo da lista
print(deq)

# Removendo elementos

print(deq.pop()) # retorna e remove o último elemento
print(deq)

print(deq.popleft()) # retorna e remove o primeiro elemento
print(deq)