pergunta_ao_usuario = input("Por favor, escolha uma entre as quatro opções abaixo:\nMultriplicação\nSoma\nSubtração\nElevado:\n")

valor_numero1 = int(input("Agora digite um número: "))
valor_numero2 = int(input("Digite outro número: "))

if pergunta_ao_usuario == "multiplicação":
    print("{} * {} = {}".format(valor_numero1, valor_numero2, (valor_numero1*valor_numero2)))
elif pergunta_ao_usuario == "soma":
    print("{} + {} = {}".format(valor_numero1, valor_numero2, (valor_numero1+valor_numero2)))
elif pergunta_ao_usuario == "subtração":
    print("{} - {} = {}".format(valor_numero1, valor_numero2, (valor_numero1-valor_numero2)))
elif pergunta_ao_usuario == "elevado":
    print("{} ** {} = {}".format(valor_numero1, valor_numero2, (valor_numero1**valor_numero2)))
else:
    print("Esta opção não é válida, favor escolher uma entre as quatro acima")
