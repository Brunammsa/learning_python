"""
Listas aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamada de arrays:
    - Unidimensionais (arrays/vetores);
    - Multidimensionais (matrizes); -esta aula-

Em python nós temos as listas:

numeros = [1, "b", 3.1, 4, True]
"""

# Exemplos
#            [0]         [1]        [2]
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3x3
print(listas)
print(type(listas))

# Como fazer para acessar os dados?
#            L  C (linha/coluna)
print(listas[0][2])

# Iterando com loops em uma lista

for lista in listas:
    for numero in lista:
        print(numero)

# Com list comprehension

[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos
# Gerando um tabuleiro de xadrez 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)