def positivo_ou_negativo(numero):
    if numero < 0:
        return -1
    elif numero == 0:
        return 0
    else:
        return 1

print(positivo_ou_negativo(23))
print(positivo_ou_negativo(0))
print(positivo_ou_negativo(-43))