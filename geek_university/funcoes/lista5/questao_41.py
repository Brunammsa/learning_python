import math

def maior_numero_do_vetor(numero):
#    maior_numero = infinito aqui
    for i in numero:
        if i > maior_numero:
            maior_numero = i
    return maior_numero

print(maior_numero_do_vetor([-4, -7, -1, -10]))