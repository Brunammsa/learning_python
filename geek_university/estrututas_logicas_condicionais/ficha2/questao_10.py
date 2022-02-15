altura = float(input("Digite sua altura: "))
sexo_usuario = input("Digite seu sexo: ")
sexo1 = "masculino"
sexo2 = "feminino"
peso_mulheres = round((62.1 * altura) - 44.7, 2)
peso_homens = round((72.7 * altura) - 58, 2) #round serve para arredondar o número, e no caso, coloquei c/ 2 casa decimais)

if sexo_usuario == sexo1:
    print("{}: peso ideal {}".format(sexo_usuario, peso_homens))
elif sexo_usuario == sexo2:
    print("{}: peso ideal {}".format(sexo_usuario, peso_mulheres))