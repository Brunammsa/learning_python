#isso é tipo um sorteio

import random
 #random.seed(1)
numero = random.randint(0,15)
print(numero)

#obs1: sempre que printar, ele dara um numero diferente.
#obs2: se quiser que o primeiro numero mantenha-se. (linha 4)

lista1 = [5, 3, 9, 25]
numero = random.choice(lista1)
print(numero)

#obs3: o modo random.choice vai aleatoriamente um numero dentro da lista já pre-determinada.