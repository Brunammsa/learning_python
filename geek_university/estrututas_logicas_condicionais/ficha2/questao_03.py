import math
numero = int(input("Digite um número inteiro: "))

if numero >= 0:
    print("{}".format(math.sqrt(numero)))
elif numero <= 0:
    print("{}".format(numero ** 2))