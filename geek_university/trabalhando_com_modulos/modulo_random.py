"""
- Módulos em Python nada mais são do que outros arquivos Python;
"""

"""
Forma 1 (não recomendada)

Ao realizar o importe de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro
do módulo ficarão disponíveis. Ficando em memória. Esta opção serve para caso você não saiba quais funções irá utilizar.
"""
import random

"""
Forma 2 (recomendada)

Agora estamos falando: Do módolo random, importe a função random.

Não disperdiçando memória
"""
from random import random

for i in range(10):
    print(random()) # random() gera um número real pseudo-aleatório de 0-1

from random import uniform

# uniform() gera um número real psudo-aleatório entre os valores estabelecidos

for i in range(10):
    print(uniform(3, 6)) # assim como no range, o 6 não é incluído

# randint gera um número inteiro pseudo-aleatório entre os valores estabelecidos

from random import randint

for i in range(7):
    print(randint(1, 61), end=', ') # começa no 1 e vai até o 60

# choice() mostra um valor aleatório entre um iterável

from random import choice
jogadas = ["pedra", "papel", "tesoura"]

print(choice(jogadas))

# shuffle() tem como ojetivo embaralhar elementos

from random import shuffle

amigos = ["bruna", "bruno", "luiz", "anna", "vanessa"] # ordem original

shuffle(amigos)

print(amigos) # agora com a ordem bagunçada
