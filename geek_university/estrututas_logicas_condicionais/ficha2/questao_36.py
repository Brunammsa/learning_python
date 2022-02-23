valor_venda = float(input("Digite o valor da venda: R$ "))

if valor_venda >= 100.000:
    print("A comissão do vendedor foi de R$ 700.00 + 16 porcento, totalidando: {}".format(700+ valor_venda*0.16))
elif valor_venda < 100.000 and valor_venda >= 80.000:
    print("A comissão do vendedor foi de R$ 650.00 + 14 porcento, totalidando: {}".format(650+ valor_venda*0.14))
elif valor_venda < 80.000 and valor_venda >= 60.000:
    print("A comissão do vendedor foi de R$ 600.00 + 14 porcento, totalidando: {}".format(600+ valor_venda*0.14))
elif valor_venda < 60.000 and valor_venda >= 40.000:
    print("A comissão do vendedor foi de R$ 550.00 + 14 porcento, totalidando: {}".format(550+ valor_venda*0.14))
elif valor_venda < 40.000 and valor_venda >= 20.000:
    print("A comissão do vendedor foi de R$ 500.00 + 14 porcento, totalidando: {}".format(500+ valor_venda*0.14))
elif valor_venda < 20.000:
    print("A comissão do vendedor foi de R$ 400.00 + 14 porcento, totalidando: {}".format(400+ valor_venda*0.14))
#preciso voltar p essa