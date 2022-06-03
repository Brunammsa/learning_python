"""
List comprehension

- Nós podemos adicionar estruturas condicionais lógicas
"""

# Exemplos
# 1

numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# 2

resultado = [numero * 2 if numero % 2 == 0 else numero / 2  for numero in numeros]
print(resultado)