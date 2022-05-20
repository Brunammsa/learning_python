def fatorial_duplo(numero_inteiro_positivo):
    multi_numero_impar = 1
    for i in range(numero_inteiro_positivo, 0, -1):
        if i % 2 != 0:
            multi_numero_impar = multi_numero_impar * i
    return multi_numero_impar

print(fatorial_duplo(5))
