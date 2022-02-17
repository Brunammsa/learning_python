opcoes = input("Por favor, escolha uma dentre as opções abaixo:\n1- Soma de dois números: \n2- Diferença entre 2 números (maior pelo menor): \n3- Produto entre 2 números: \n4- Divisão entre 2 números (o denominador não pode ser 0)\n")

numero1 = int(input("Agora escolha o primeiro número: "))
numero2 = int(input("Escolha o segundo número: "))

if opcoes == "1":
    print("{} + {} = {}".format(numero1, numero2, numero1+numero2))
elif opcoes == "2":
    if numero1 > numero2:
        print("a diferença entre {} e {} é {}".format(numero1, numero2, numero1-numero2))
    elif numero2 > numero1:
        print("a diferença entre {} e {} é {}".format(numero2, numero1, numero2-numero1))
elif opcoes == "3":
    print("{} * {} = {}".format(numero1, numero2, numero1*numero2))
elif opcoes == "4":
    if numero2 == 0:
        print("Não é possível que o denominador seja 0, por favor, tente novamente")
    else:
        print("{} / {} = {}".format(numero1, numero2, numero1/numero2))
