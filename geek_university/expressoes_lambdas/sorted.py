"""'
Sorted

- Não confundir sorted com sort(), visto em listas, e apenas. Atualiza a lista ordenando-a
- Podemos utilizar o sorted() com qualquer iterável. Mantém-se a lista e cria outra ordenada

sorted() serve para ordenar
"""

# OSB.: pode-se adc parâmetros ao sorted()

numeros = [6, 8, 2, 10]

print(sorted(numeros, reverse=True))

# Podemos utilizar o sorted() para coisas mais complexas

# Exemplo 1
usuarios = [
    {"username": "tenorio", "tweets": []},
    {"username": "bruna", "tweets": ["eu amo caranguejo", "amo dormir", "gosto de assistir pantanal"]},
    {"username": "felipe", "tweets": ["adoro diablo immortal", "e assistir anime"]},
    {"username": "bruno", "tweets": [], "cor": "amarelo"},
    {"username": "vanessa", "tweets": ["bora tomar uma breja"], "cor": "preto", "musica": "rock"}
]

print(usuarios)
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

# Exemplo 2

musicas = [
    {"titulo": "O seu amor me persegue", "tocou": 3},
    {"titulo": "Yeshua", "tocou": 5},
    {"titulo": "Fumaça", "tocou": 2},
    {"titulo": "Faz arder", "tocou": 4}
]

print(sorted(musicas, key=lambda musica: musica["tocou"])) # crescente
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True)) # decrescente