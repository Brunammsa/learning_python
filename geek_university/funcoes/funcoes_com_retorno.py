numeros = [1, 2, 3]

ret_pop = numeros.pop()
print('retorno de pop {}'.format(ret_pop))

ret_pop = print(numeros)
print('retorno de print {}'.format(ret_pop))

# Exemplo função

def quadrado_de_7():
    return 7 * 7

ret = quadrado_de_7()
print('retorno {}'.format(ret))
print('retorno {}'.format(quadrado_de_7()))
'''
OBS.: Em Python, quando uma função não retorna nenhum valor, o retorno é None;
OBS.: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return;
OBS.: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções;
'''

# Refatorando a primeira função (reescrevendo)

def diz_oi():
    return 'Oi, '
#   print('Oi, ') se for com print, sem o return, não conseguiremos printar da forma que está;
alguem = 'Bruna!'
print(diz_oi() + alguem) # precisamos utilizar o diz_oi sozinho e printar o alguém no print;

''' OBS.: Sobre a palavra reservada return

1- Ela finaliza a função, ou seja, ela sai da execução da função;
2- Podemos ter, em uma função, diferentes returns;
3- Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
'''

# Exemplo 1

def diz_oi():
    print('estou sendo executado após o retorno')
    return 'Oi ' # após  return, NADA é executado, acaba aqui
    print('estou sendo executado após o retorno')

print(diz_oi())

# Exemplo 2

def nova_funcao():
    variavel = False # esse é o x da questão para o if, elif e return final
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b' # aqui é como se fosse um else:

print(nova_funcao())

# Exemplo 3

def outra_funcao():
    return 2, 3, 4, 5 # retornou tupla

num2, num3, num4, num5 = outra_funcao()

print(outra_funcao())

# Vamos criar uma função para jogar cara ou coroa

from random import random

def joga_moeda():
    # gera um número pseudo randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return "cara"
    return 'coroa'

print(joga_moeda())

# Erros comuns na utilização do return, mas que na verdade, nem é erro, mas sim codificação desnecessária.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
