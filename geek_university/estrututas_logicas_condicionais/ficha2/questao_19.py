numero = int(input("Digite um número e descubra se ele é divisível por 3 ou por 5: "))

if numero %3 == 0:
    print("{} é divisível por 3". format(numero))
elif numero %5 == 0:
    print("{} é divisível por 5".format(numero))
else:
    print("{} não é divisível por 3 nem por 5, por favor, tente novamente".format(numero))