import math

numero = int(input("Digite um número: "))

if numero %2 == 0:
    print("a raiz quadrada do número {} é {}".format(numero, math.sqrt(numero)))
else:
    print("o número é invalido")