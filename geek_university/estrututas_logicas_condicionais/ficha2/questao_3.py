import math
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("{}".format(math.sqrt(numero)))
else:
    print("{}".format(numero ** 2))