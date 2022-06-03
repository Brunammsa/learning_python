"""
Set comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4,5} # não guarda ordenação, não aceita repetidos
"""

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Desafio: Faça uma obs na estrutura acima para gerar um dict ao invés de set

set_to_dict = {x:x ** 2 for x in range(10)}
print(set_to_dict)

letras = {letra for letra in "Hello world"}
print(letras)