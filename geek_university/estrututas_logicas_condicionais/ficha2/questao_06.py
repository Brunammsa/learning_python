numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
    print("o número {} é o maior e a diferença entre eles é de {}".format(numero1,(numero1-numero2)))
else:
    print("o número {} é o maior e a diferença entre eles é de {}".format(numero2, (numero2-numero1)))