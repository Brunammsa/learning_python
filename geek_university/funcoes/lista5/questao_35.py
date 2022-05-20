from questao_20 import fatorial

# modo mundo real
def fatorial_quadruplo(numero):
    dobro_do_numero = 2 * numero
    quadruplo = fatorial(dobro_do_numero)/fatorial(numero)
    return quadruplo

print(fatorial_quadruplo(2))

# modo cornojob
def fatorial_cornojob(numero):
    primeirio_fatorial = 2 * numero
    segundo_fatorial = numero

    multiplicador_primeiro_fat = 1
    for i in range(primeirio_fatorial, 0, - 1):
        multiplicador_primeiro_fat *= i

    multiplicador_segundo_fat = 1
    for j in range(segundo_fatorial, 0, -1):
        multiplicador_segundo_fat *= j

    quadruplo = multiplicador_primeiro_fat/multiplicador_segundo_fat
    return quadruplo

print(fatorial_cornojob(2))
