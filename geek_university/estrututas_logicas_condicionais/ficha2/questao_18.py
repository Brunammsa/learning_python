pergunta_ao_usuario = input("Por favor, escolha uma entre as quatro opções abaixo:\nMultiplicação\nSoma\nSubtração\nDivisão:\n")

valor_numero1 = float(input("Agora digite um número: "))
valor_numero2 = float(input("Digite outro número: "))

if pergunta_ao_usuario == "Multiplicação":
    print("{} * {} = {}".format(valor_numero1, valor_numero2, round(valor_numero1*valor_numero2, 2)))
elif pergunta_ao_usuario == "Soma":
    print("{} + {} = {}".format(valor_numero1, valor_numero2, (valor_numero1+valor_numero2)))
elif pergunta_ao_usuario == "Subtração":
    print("{} - {} = {}".format(valor_numero1, valor_numero2, (valor_numero1-valor_numero2)))
elif pergunta_ao_usuario == "Divisão":
    if valor_numero2 == 0:
        print("Não é possível realizar divisões por 0, por favor, digite um número válido")
    else:
        print("{} ** {} = {}".format(valor_numero1, valor_numero2, (valor_numero1/valor_numero2)))
else:
    print("Esta opção não é válida, favor escolher uma entre as quatro acima")
