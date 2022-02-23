numero1 = int(input("Digite um número qualquer: "))
numero2 = int(input("Digite outro número qualquer: "))
numero3 = int(input("Digite mais um número qualquer: "))

if numero1 <= numero2 and numero1 <= numero3 and numero2 <= numero3:
    print("A ordem crescente é {} {} {}".format(numero1, numero2, numero3))
elif numero1 <= numero2 and numero1 <= numero3 and numero3 <= numero2:
    print("A ordem crescente é {} {} {}".format(numero1, numero3, numero2))
elif numero2 <= numero1 and numero2 <= numero3 and numero1 <= numero3:
    print("A ordem crescente é {} {} {}".format(numero2, numero1, numero3))
elif numero2 <= numero1 and numero2 <= numero3 and numero3 <= numero1:
    print("A ordem crescente é {} {} {}".format(numero2, numero3, numero1))
elif numero3 <= numero1 and numero3 <= numero2 and numero1 <= numero2:
    print("A ordem crescente é {} {} {}".format(numero3, numero1, numero2))
elif numero3 <= numero1 and numero3 <= numero2 and numero2 <= numero1:
    print("A ordem crescente é {} {} {}".format(numero3, numero2, numero1))
else:
    print("Valores inválidos, por favor tente novamente")



