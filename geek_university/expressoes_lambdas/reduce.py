"""
Reduce

OBS.: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar e utilizar esta função a partir do
módolo 'functools'

Para entender o reduce()

Imagine que você tem uma coleção de dados e uma função que recebe dois parâmetros: reduce(funcao, dados)

dados = [a1, a2, a3...an]

def funcao(x, y):
    retur x * y

A função reduce funciona da seguinte forma:
Passo 1:
res1 = f(a1, a2) Aplica a função noa dois primeiros elementos da coleção e guarda o resultado.

Passo 2:
res2 = f(res1, a3) Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o resultado e continua assim até o final.

No final de tudo, o reduce() irá retornar o resultado final.
"""


from functools import reduce

# Na prática com lambda:

dados = [1, 2, 3, 5, 2, 4, 1, 2]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando loop normal:

res = 1
for n in dados:
    res = res * n


print(res)
