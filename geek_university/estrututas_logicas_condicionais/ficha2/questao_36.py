valor_venda = float(input("Digite o valor da venda: R$ "))


porcentagem_comissao1 = valor_venda * 0.14
porcentagem_comissao2 = valor_venda * 0.16
print(porcentagem_comissao1)
print(porcentagem_comissao2)


if valor_venda < 20000:
    print("A comissão do vendedor foi de R$ 400.00 + 14 porcento, totalidando: {}".format(400+porcentagem_comissao1))
elif valor_venda >= 20000 and valor_venda < 40000:
    print("A comissão do vendedor foi de R$ 500.00 + 14 porcento, totalidando: {}".format(500+porcentagem_comissao1))
elif valor_venda >= 40000 and valor_venda < 60000:
    print("A comissão do vendedor foi de R$ 550.00 + 14 porcento, totalidando: {}".format(550+porcentagem_comissao1))
elif valor_venda >= 60000 and valor_venda < 80000:
    print("A comissão do vendedor foi de R$ 600.00 + 14 porcento, totalidando: {}".format(600+porcentagem_comissao1))
elif valor_venda >= 80000 and valor_venda < 100000:
    print("A comissão do vendedor foi de R$ 650.00 + 14 porcento, totalidando: {}".format(650+porcentagem_comissao1))
elif valor_venda >= 100000:
    print("A comissão do vendedor foi de R$ 700.00 + 16 porcento, totalidando: {}".format(700+porcentagem_comissao2))
