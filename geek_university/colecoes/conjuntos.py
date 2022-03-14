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
"""
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

# Num Sets podemos incluir qualquer tipo de dado

conjunto = {2, 'bruna', True, 34.22, 11}
print(conjunto)
print(type(conjunto))

# Podemos iterar um Sets

for elementos in conjunto:
    print(elementos)

# Adicionando elementos aos Sets

conjunto = {1, 2, 3}
print(conjunto)
conjunto.add(4)
print(conjunto)

# Removendo elementos

conjunto.remove(4) # forma 1 // se não existir o elemento a ser removido, dará KeyError
print(conjunto)

conjunto.discard(3) # forma 2 // se não existir o elemento a ser removido, não dará erro
print(conjunto)

# Copiando um conjunto para outro // Deep copy, a mudança acontece apenas no novo conjunto, o original se mantém
conjunto = {1, 2, 3}
print(conjunto)

novo_conjunto = conjunto.copy()
print(novo_conjunto)

novo_conjunto.add(4)

print(novo_conjunto)
print(conjunto)

# Forma 2 // Shallow copy, ambos os conjuntos são modificados
conjunto = {1, 2, 3}
print(conjunto)

novo_conjunto = conjunto
novo_conjunto.add(4)

print(conjunto)
print(novo_conjunto)

# Podemos remover todos os itens de um conjunto

conjunto = {1, 2, 3}
print(conjunto)

conjunto.clear()
print(conjunto)

# Métodos matemáticos de conjuntos

# ex.: temos dois conjuntos de alunos, 1 estudam python, outro estudam java, alguns alunos estudam python e java

alunos_python = {'Bruna', 'Bruno', 'Lucas', 'Leo'}
alunos_java = {'Bruno', 'Victor', 'Daniel', 'Lucas', 'Hugo'}

# Gerando um conjunto com o nome dos estudantes // forma 1

estudantes_geral = alunos_python.union(alunos_java) # não importa a ordem // forma mais clara
print(estudantes_geral)

# forma 2 utilizando pipe |

estudantes_geral2 = alunos_python | alunos_java
print(estudantes_geral2)

# Gerando um conjunto que ambos os cursos
# Forma 1 // intersection

ambos_cursos = alunos_python.intersection(alunos_java)
print(ambos_cursos)

# forma 2 // &

ambos_cursos2 = alunos_python & alunos_java
print(ambos_cursos2)

# Gerando conjunto de estudantes que não estão nos dois cursos

so_py = alunos_python.difference(alunos_java)
print(so_py)

so_java = alunos_java.difference(alunos_python)
print(so_java)

# Soma*, valor máximo, valor mínimo, tamanho
# *valores inteiros e reais
conjunto = {1, 2, 3, 4, 5, 6, 7}

print(sum(conjunto))
print(max(conjunto))
print(min(conjunto))
print(len(conjunto))