"""
Min e Max

- max() retorna o maior valor em um iterável ou o maior de dois ou mais elementos;
- min() retorna o menor valor em um iterável ou o menor de dois ou mais elementos;
"""

# Exemplos

valores = [9, 3, 56, 2, 765, 8, 5, 67]
print(max(valores))
print(min(valores))

nomes = ["Bruna", "Luiz Felipe", "Gleice", "Anna", "Vanessa"]

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {"titulo": "O seu amor me persegue", "tocou": 3},
    {"titulo": "Yeshua", "tocou": 5},
    {"titulo": "Fumaça", "tocou": 2},
    {"titulo": "Faz arder", "tocou": 8}
]

print(max(musicas, key=lambda musica: musica["tocou"])["titulo"]) # imprimir o título da música
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])

# Agora sem max e min

max = 0
for musica in musicas:
    if musica["tocou"] > max:
        max = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == max:
        print(musica["titulo"])

min = 9999
for musica in musicas:
    if musica["tocou"] < min:
        min = musica["tocou"]

for musica in musicas:
    if musica["tocou"] == min:
        print(musica["titulo"])
