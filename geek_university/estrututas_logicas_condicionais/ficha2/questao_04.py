import math
numero = int(input("Digite um número: "))

if numero >= 0:
    print("{}".format(numero ** 2))
    print("{}".format(math.sqrt(numero)))
else:
    print("Número inválido, digite um número positivo")