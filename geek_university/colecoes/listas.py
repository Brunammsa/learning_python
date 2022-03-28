'''
Listas

Listas em python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO e também poderem colocar qualquer tipo de dado.

Dinâmico: não possue tamanho fixo, ou seja, podemos criar uma lista e simplesmente ir adicionando elementos
'''

# Ex.:

lista1 = [1, 6, 33, 2, 6, 8, 3, 0]
lista2 = ['b', 'r', 'u', 'n', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('Bruna')
cores = ['vede', 'amarelo', 'azul']



# Checando se um elemento está dentro da lista:

num = 3

if num in lista4:
    print('Esta dentro da lista')
else:
    print('Não está dentro da lista')

# Ordenando uma lista

lista1.sort()
print(lista1)

# Podemos contar a quantidade de elementos numa lista

print(lista1.count(6))
print(lista5.count('u'))

# Para adicionar elementos a uma lista
# OBS.: com append só conseguimos adicionar um elemento por vez

lista1.append(29) # *** COM APPEND ***
print(lista1)

#OBS.: mas podemos colocar uma lista dentro de uma lista

lista1.append([98, 44, 100]) # lista como elemento único
print(lista1)

if [98, 44, 100] in lista1:
    print('encontrei a lista')
else:
    print('não encontrei a lista')

lista1.extend([29, 30]) # *** COM EXTEND *** ele não entra como lista, mas precisa dos []
print(lista1)

lista1.extend('bruna') # é possível passar str
print(lista1)

#OBS.: o append ou extend sempre atribui o valor ao final da lista

# Podemos inserir um novo elemento na posição desejada

lista1.insert(2, 'hello') # (posição, elemento)
print(lista1)

# Podemos juntar listas criando uma nova ou utilizando o extend

lista6 = lista1 + lista2
print(lista6)

lista1.extend(lista2)
print(lista1)


# Podemos inverter listas

print(lista1)
lista1.reverse() # *** COM RESERVE *** não ta selecionando o comando mas ta pegando (só ta pegando com int)
print(lista1)

print(lista2[::-1]) # deveria inverter int também, mas não ta pegando por alguma razão, se chama slice, [começa na posição 0:vai até o final:e inverte]

# Podemos copiar uma lista criando outra

lista6 = lista2.copy()
print(lista6)

# Como saber o tamanho da lista, contando quantos elementos existem dentro da lista

print(len(lista1))

# Podemos remover o último elemento de uma lista

print(lista1)
lista1.pop(3) # () vazio ele remove o último, ou podemos inserir a posição que desejamos excluir
print(lista1)

# Podemos remover todos os elementos de uma lista

print(lista1)
lista1.clear() # o comando não está selecionado no meu python, mas funciona normal
print(lista1)

# Podemos repetir listas (multiplica-las)

lista2 = lista2 * 2
print(lista2)

# Podemos transformar uma str em lista

nome = 'bruna de melo'
nome = nome.split() # separador por espaços
print(nome)

nome = 'bruna,de,melo'
nome = nome.split(',') # separador por ','
print(nome)

# Convertendo uma lista em str

lista7 = ['bruna', 'de', 'melo']
lista8 = ' '.join(lista7) # atribuindo a uma nova variável // aqui foi atribuído espaço entre cada elemento, mas pode ser qualqur coisa
print(lista8)

# Iterando sobre listas
soma = 0
for i in lista1:
    print(i)
    soma += i
print(soma)

carrinho = []
produto = ''

while produto != 'sair':
    print('Adicione um produto ou digite "sair" para finalizar')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Pode-se utilizar variáveis dentro de listas

num1 = 1
num2 = 2
num3 = 3
num4 = 4

numeros = [num1, num2, num3, num4]
print(numeros)

# Podemos acessar elementos de forma indexada

print(cores[2])
print(cores[-1]) # se utilizarmos [-posição] ele irá ler de tras para frente, -1 sendo o último

for cor in cores:
    print(cor)

indice = 0

while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerando índice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam repetições

lista = []
lista.append(33)
lista.append(44)
lista.append(33)
lista.append(23)

print(lista)

# Outros métodos não tão importantes, porém interessantes

# Encontrando o índice de um elemento na lista

amigos = ['bruna','bruno', 'anna', 'felipe', 'bruna']
print(amigos.index('anna')) # em qual posição está anna?
print(amigos.index('bruna')) # quando houver duplicidade de elemento dentro da lista, ele retornará o primeiro encontrado
print(amigos.index('bruna', 1)) # podemos utilizar a forma range para definirmos a partir de que elemento ele comece a busca (elemento, posicao de início)
print(lista1.index(8, 2, 7)) # (elemento, posição de início, posição final de busca)

# Revisando Slicing

# Lista[inicio, fim, passo]
# range[inicio, fim, passo]

print(lista1[1:]) # da posição 1 até o final
print(lista1[:2]) # do início até o 1, exclui-se o 2, que é o limite (igual range mesmo)
print(lista1[::]) # do início ao fim, sem restrição
print(lista1[::-1]) # como já visto anteriormente, inicia ao contrário
print(lista1[::2]) # do início ao fim de dois em dois

# Invertendo valores em uma lista

nomes = ['bruna', 'melo']

nomes[0], nomes[1] = nomes[1], nomes[0] # opção 01
print(nomes)

nomes.__reversed__() # só ta pegando com str
print(nomes)

# Soma, valor máximo, valor mínimo e tamanho

print(sum(lista1))
print(max(lista1))
print(min(lista1))
print(len(lista1))

# Transformar lista em tupla

print(tuple(lista1)) # por enquanto, percebe-se que a diferença é a troca dos [] por () (estudarei tupla na próxima aula)

# Desempacotamento de lista
lista = [1, 2, 3]

num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Copiando uma lista para a outra (shallow copy, deep copy)

nova = lista.copy() # cópia
print(nova)

nova.append(4) # dessa forma, estaremos criando uma nova lista acrescentando um número a mais, totalmente indepentende da lista copiada. DEEP COPY
print(nova)

nova = lista # cópia # SHALLOW COPY, ambas as listas foram modificadas  
nova.append(4)
print(nova)
print(lista)

