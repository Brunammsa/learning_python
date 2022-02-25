from sys import float_repr_style


custo_fabrica = float(input("Digite o custo de fábrica do carro novo: R$ "))

if custo_fabrica < 12000:
    print("O custo do consumidor é de R$ {}".format(custo_fabrica + (custo_fabrica*0.05)))
elif custo_fabrica > 12000 and custo_fabrica < 25000:
    print("O custo do consumidor é de R$ {}".format(custo_fabrica + (custo_fabrica*0.10) + (custo_fabrica*0.15)))
elif custo_fabrica > 25000:
    print("O custo do consumidor é de R$ {}".format(custo_fabrica + (custo_fabrica*0.15) + (custo_fabrica*0.20)))

