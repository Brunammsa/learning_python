"""
Utilizando list comprehension:

- podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe:
[ dado for dado in interável ]

"""

# Exemplo

numeros = [1, 2, 3, 4, 5]

resultado = [numero * 10 for numero in numeros] # lê-se ao contrário: para cada número em numeros, multiplique numero por 10
print(resultado)

resultado = [numero / 2 for numero in numeros]
print(resultado)

def funcao(valor):
    return valor * valor

resultado = [funcao(numero) for numero in numeros]
print(resultado)

numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# usando list comprehension

print([numero * 2 for numero in numeros])

# Outros exemplos

# 1

none = 'Hello world'

print([letra.upper() for letra in none])

# 2

def maiusculo(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


lista_amigos = ['bruno', 'julia', 'tenório', 'gleice', 'vanessa']
print([maiusculo(amigo) for amigo in lista_amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 2, 3]])

# 5

print([str(numero) for numero in [1, 2, 3, 4]])