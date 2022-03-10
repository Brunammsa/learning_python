# Tuplas

# São parecidas com as listas.

# diferenças básicas:

# 1- são representadas por () quando imprimidas
# 2- São imutáveis: ao criar uma tupla, ela não muda, toda operação em uma tupla, gera uma nova tupla

# CUIDADO

tupla1 = (1, 2, 3, 4, 5)
print(type(tupla1))
print(tupla1)

tupla2 = 1, 2, 3, 4, 5 # mesmo sem os parênteses, ele reconhece como tupla
print(type(tupla2))
print(tupla2)

# OBS: tuplas são feitas com 2 ou mais elementos
# OBS: Podemos dizer que tuplas são definidas pela virgula e não necessariamente pelo ()

# (4) não é tupla
# (4,) é tupla
# (4, 5,) é tupla
# (4, 5, 6) é tupla
# 4, é tupla
# 4, 5, 6 é tupla

# Podemos gerar uma tupla com range

tupla3 = tuple(range(6))

# Da mesma forma que há a possibilidade de desempacotamento na lista, também há na tupla

tupla4 = ('Bruna', 'Melo')
nome, sobrenome = tupla4
print(nome)
print(sobrenome)

# Métodos para: Adição e remoção de elementos nas tuplas não existe, pois as tuplas são imutáveis

# Soma, valor máximo, valor mínimo e tamanho *** Os valores sendo reais ou reais, ta valendo ***

tupla4 = (1, 2, 3, 4, 5, 6, 7)
print(sum(tupla4))
print(max(tupla4))
print(min(tupla4))
print(len(tupla4))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla1)
print(tupla2)

print(tupla1 + tupla2) # concatenação, juntou as duas tuplas, e quando imprimi novamente elas separadas abaixo, elas voltaram ao normal

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2 # criei nova tupla com a concatenação das duas anteriores
print(tupla3)

tupla1 = tupla1 + tupla2 # você pode também sobrescrever os valores de uma tupla
print(tupla1)

# Verificando se determinado elemento esta contido na tupla

print(33 in tupla1) # como se fosse um if, masi assim ele vai retornar True or False

# Iterando sobre uma tupla

tupla1 = (1, 2, 3)

for i in tupla1:
    print(i)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla0 = ('a', 'b', 'c', 'd', 'e')
print(tupla0.count('b')) # assim como na lista, o count imprime a posição do elemento solicitado

faculdade = tuple('Faculdade dos Guararapes') # transformando uma str em tuple
print(faculdade)
print(faculdade.count('a')) # quandos 'a' tem na tupla faculdade

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# você não pode por ex usar um append para acrescentar um elemento como numa lista, e se você quer uma variável não modificável, o aconselhável é fazer uma tupla

# Os elementos de uma tupla também se assemelham a uma lista

print(meses[4]) # localizando o mês na posição 4

# Podemos iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificando se um elemento encontra-se na tupla

print(meses.index('Junho')) # ele retorna a posição em que se encontra o elemento, caso não tenha, ele retornara ValueError, e se tiver duplicidade, irá imprimir o primeiro encontrado

# Slicing
# tuplas[inicio: fim: passo]

# Por quê utilizar tuplas?

# São mais rápidas do que listas
# São mais seguras, pois são imutáveis

# Copiando uma tupla, não temos o problema de shallow copy como na lista

tupla = (1, 2, 3)
print(tupla)

nova_tupla = tupla # copiando a tupla
print(nova_tupla)

outra_tupla = (4, 5, 6)
nova_tupla = nova_tupla + outra_tupla
print(nova_tupla)

print(tupla)
print(nova_tupla)