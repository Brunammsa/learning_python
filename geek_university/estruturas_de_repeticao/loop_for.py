# Looping for

"""
for item in iterável: (Para cada item dentro deste iterável)
    //execução do loop
"""

# Utiliza-se o loop para iterar sobre sequências ou sobre valores iteráveis

"""
Exemplos de iteráveis:

- String
    variavel = "Hello word"
- Lista
    lista = [1, 2, 3, 4]
- range
    numeros = range(1, 5)


# Exemplos:

# String
nome = "hello word"
for letras in nome:
    print(letras)

# Lista

lista = [1, 2, 3, 4, 5]

for numeros in lista:
    print(numeros)

#Range
# range(valor_inicial, valor_final) // Lembrando que no range o último valor é descartado, no caso, o 6

for posicoes in range(1, 6): 
    print(posicoes)


Enumerate:

nome = "Hello Word"
((0, "H"), (1, "e"), (2, "l"), (3, "l"), (4, "o""), (5, " "), (6, "W"), (7, "o"), (8, "r"), (9, "d"))

Ex.:
for indice, letras in enumerate(nome):
    print(nome[indice])

for indice, letras in enumerate(nome):
    print(letras)

for _, letras in enumerate(nome): # Quando não precisamos de um valor, podemos descartalo - _
    print(letras)

for valor in enumerate(nome):
    print(valor) # Por dentro do print [0] ou [1] quer dizer printar apenas as posições ou apenas as letras


quantidade = int(input("Quantas vezes rodar o loop? "))

for n in range(1, quantidade):
    print("Imprimir {}".format(n))

soma = 0

for n in range(1, quantidade+1):
    numero = int(input("Informe um número de {} até {}: ".format(n, quantidade)))
    soma = soma + numero
print("a soma é {}".format(soma))

# Caso eu não queira que ele print linha por linha:

for letras in nome:
    print(letras, end="")


# Curiosidades:

Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

Original =  U+1F63B
modificado = U0001F63B
"""
