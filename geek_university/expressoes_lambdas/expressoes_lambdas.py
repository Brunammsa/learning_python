"""
Utilizando lambdas:

Conhecidas como expressões lambdas, ou simplesmente por lambdas, são funções sem nome, ou seja, funções anônimas.

"""
# Função em Python

def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão lambda

lambda x: 3 * x + 1

aqui_por_o_nome_para_o_lambda = lambda x: 3 * x + 1

print(aqui_por_o_nome_para_o_lambda(4))

# OBS1.: Podemos ter expressões lambdas com multiplcas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('bruna', 'melo'))

# OBS2.: Em funções Python podemos ter várias entradas ou até mesmo nenhuma. Em lambda também!

# Outros exemplos

amigos = ['bruno barros a.', 'vanessa', 'julia maria lins de barros', 'nathalia rocha']

amigos.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(amigos)

# Função quadrática

# f(x) = a * x ** 2 + b * x + c

# definindo a função

def geradora_funcao_quadratica(a, b, c):
    """ retorna f(x) = a * x ** 2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))