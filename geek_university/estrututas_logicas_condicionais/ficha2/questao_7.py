numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

if numero1 > numero2:
    print("{} é o maior do que {}".format(numero1, numero2))
elif numero2 > numero1:
    print("{} é maior do que {}".format(numero2, numero1))
elif numero2 == numero1:
    print("números iguais")