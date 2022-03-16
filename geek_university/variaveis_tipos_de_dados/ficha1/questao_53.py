dimensao_comprimento = int(input("digite a dimensao do comprimento do terreno: "))
dimensao_largura = int(input("digite a dimensao da largur do terreno: "))
preço_metro_tela = int(input("digite o preco do metro em tela: R$ "))
calculo1 = dimensao_comprimento * preço_metro_tela
calculo2 = dimensao_largura * preço_metro_tela

print("o custo para cercar o terreno com tela no comprimento eh de: R$ {}".format(calculo1))
print("o custo para cercar o terreno com tela na largura eh de: R$ {}".format(calculo2))