"""
Poderíamos chamar este parâmetro de **args, mas por convenção chamamos de kwargs;

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que utilizemos parâmetros
nomeados, e transforma estes parâmetros extras em um dict;
"""

# Exemplo
from geek_university.funcoes.entendendo_args import soma


def cores_favorias(**kwargs):
    for pessoa, cor in kwargs.items():
        print('a cor favorita de {} é {}'.format(pessoa, cor))

cores_favorias(vanessa='azul', bruna='amarelo', felipe='preto')

# OBS.: os parâmetros *args e **kwargs não são obrigatóris

"""
Nas funções, podemos ter (NESTA ORDEM):
- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs
"""

# ordem correta
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print('{} tem {} anos'.format(nome, idade))
    print(args)
    if solteiro:
        print('solteiro(a)')
    else:
        print('casado(a)')
    print(kwargs)

minha_funcao(8, 'julia')
minha_funcao(28, 'bruna', 1, 2, 3, solteiro=False)
minha_funcao(27, 'felipe', 2, 3, 4, java=False, python=True)

# desempacotando com **kwargs

def mostra_nomes(**kwargs):
    return "{} {}".format(kwargs['nome'], kwargs['sobrenome'])

nomes = {'nome':'bruna', 'sobrenome': 'melo'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)
