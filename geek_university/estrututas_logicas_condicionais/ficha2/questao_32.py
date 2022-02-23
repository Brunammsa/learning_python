cardapio = int(input("""Olá, digite o código do produto que deseja:
produtos /  código / preço
Cachorro quente - 100 - R$ 1.20
Bauro Simples - 101 - R$ 1.30
Bauro com ovo - 102 - R$ 1.50
Hambúrguer - 103 - R$ 1.20
Cheeseburguer - 104 - R$ 1.70
Suco - 105 - R$ 2.20
Refrigerante - 106 - 1.00\n
"""))
quantidade = int(input("Digite a quantidade do produto que deseja: "))

if cardapio == 100:
    print("Seu pedido ficou: {} {} por R$ {}".format(quantidade, "Cachorro(s) quente", quantidade*1.20))
elif cardapio == 101:
    print("Seu pedido ficou: {} {} por R$ {}".format(quantidade, "Bauru(s) simples", quantidade*1.30))
elif cardapio == 102:
    print("Seu pedido ficou: {} {} por R$ {}".format(quantidade, "Bauro(s) com ovo", quantidade*1.50))
elif cardapio == 103:
    print("Seu pedido ficou: {} {} por R$ {}".format(quantidade, "Hambúrguer(ers)", quantidade*1.20))
elif cardapio == 104:
    print("Seu pedido ficou: {} {} por R$ {}".format(quantidade, "Cheeseburguer(ers)", quantidade*1.70))
elif cardapio == 105:
    print("Seu pedido ficou: {} {} por R$ {}".format(quantidade, "Suco(s)", round(quantidade*2.20, 2)))
elif cardapio == 106:
    print("Seu pedido ficou: {} {} por R$ {}".format(quantidade, "Refrigerante(s)", quantidade*1.00))
else:
    print("Este valor está inválido, por favor tente novamente")
