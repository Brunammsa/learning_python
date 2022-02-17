altura = float(input("Digite sua altura: "))
sexo_usuario = input("Digite seu sexo: ")

peso_mulheres = round((62.1 * altura) - 44.7, 2)
peso_homens = round((72.7 * altura) - 58, 2) #round serve para arredondar o número, e no caso, coloquei c/ 2 casa decimais)

if sexo_usuario == "masculino":
    print("{}: peso ideal {}".format(sexo_usuario, peso_homens))
elif sexo_usuario == "feminino":
    print("{}: peso ideal {}".format(sexo_usuario, peso_mulheres))
    