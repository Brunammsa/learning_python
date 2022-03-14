"""
Conjuntos

Em Python, conjuntos são chamados de sets
- Não possuem valores duplicados;
- Não possuem valores ordenados;
- Elementos não são acessados via índice, não são index;
- Não precisamos nos preocupar com a ordenação deles;

São referenciados por {}

Diferença entre dicts e sets
    - dicts tem chave:valor
    - conjuntos tem apenas valor

# Definindo um conjunto

# Forma 1
conjunto = set({1, 2, 3, 4, 4, 5, 6, 7, 1, 4, 2, 2}) # mesmo com elementos iguais, ele não os imprime
print(conjunto)
print(type(conjunto))

# Forma 2 // mais comum
conjunto = {1, 2, 4, 3, 5, 6, 5, 7} # mesmo desordenado, ele imprime na ordem
print(conjunto)
print(type(conjunto))

# Verificando se há o elemento solicitado no conjunto

if 15 in conjunto:
    print('está contido no conjunto')
else:
    print('não esta contido no conjunto')

# Comparando com o que já aprendemos

lista = [11, 44, 2, 5, 44, 7, 3, 9, 88, 4] # imprime normal
print(lista)

tupla = 11, 44, 2, 5, 44, 7, 3, 9, 88, 4 # imprime normal
print(tupla)

dicionário = {}.fromkeys([11, 44, 2, 5, 44, 7, 3, 9, 88, 4], 'dict') # imprime sem repetição
print(dicionário)

conjunto =  {11, 44, 2, 5, 44, 7, 3, 9, 88, 4} # imprime sem repetição
print(conjunto)
"""
# Num Sets podemos incluir qualquer tipo de dado

conjunto = {2, 'bruna', True, 34.22, 11}
print(conjunto)
print(type(conjunto))

# Podemos iterar um Sets

for elementos in conjunto:
    print(elementos)