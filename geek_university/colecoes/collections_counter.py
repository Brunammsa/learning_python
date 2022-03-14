"""
Counter: Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dict, contendo como chave o elemento da lista
passada como parâmetro e com valor a quantidade de ocorrências desse elemento.

"""
# Fazendo o import

from collections import Counter

# Podemos utilizar qualquer iterável, como ex. usaremos uma lista

lista = [2, 4, 2, 6, 2, 7, 8, 66, 3, 44, 2, 33, 5, 7, 90, 88, 78]

# Utilizando o Counter

resultado = Counter(lista)

print(type(resultado))
print(resultado)

print(Counter('Paralelepipedo'))

save_ur_tears = """ you could've asked me why i broke your heart
you could've told me that you fell apart
but you walked past me like i wasn't there
and just pretended like you didn't care """

palavras = save_ur_tears.split()
print(palavras) # primeiro a gente separa cada palavra tornando-o um elemento único

resultado2 = Counter(palavras)
print(resultado2)

# para saber as palavras mais comuns:

print(resultado2.most_common(4)) # você define a quantidade de palavras/elementos mais comuns
