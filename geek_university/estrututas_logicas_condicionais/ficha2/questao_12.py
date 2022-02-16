import math

numero_inteiro = int(input("Digite um número inteiro: "))

if numero_inteiro < 0:
    print("Número inválido")
else:
    print(math.log10(numero_inteiro))