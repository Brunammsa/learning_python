"""
Dictionary comprehension

Se quisermos criar uma lista fazemos:
lista = [1, 2, 3, 4, 5]

Se quisermos fazer uma tupla:
tupla= (1, 2, 3, 4, 5)

Se quisermos criar um set (conjunto):
conjunto = {1, 2, 3, 4,5 }

Se quisermos criar um dict:
dict = {'a': 1, 'b': 2, 'c': 3}

- Sintaxe:

{chave:valor for valor in iterável}

"""

# Exemplos

numeros = {'a':1, 'b': 2, 'c':3, 'd':4, '5':5}

quadrado =  {chave:valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

lista_numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in lista_numeros}
print(quadrados)

chaves = "abcd"
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplos com condicionais

numeros = [1, 2, 3, 4, 5]
resultado = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(resultado)