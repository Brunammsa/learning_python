from random import randint

def numeros_aleatorios(numero_min, numero_max):
    numeros_aleatorios_não_repetidos = []

    while len(numeros_aleatorios_não_repetidos) != 4:
        num_aleatorios = randint(numero_min, numero_max)

        if num_aleatorios not in numeros_aleatorios_não_repetidos:
            numeros_aleatorios_não_repetidos.append(num_aleatorios)

    return numeros_aleatorios_não_repetidos
    
print(numeros_aleatorios(1, 20))
