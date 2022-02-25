preco_antigo = float(input(""" Tabela preço antigo:
Até R$ 50 - 5 porcento de aumento
Entre R$ 50 e R$ 100 - 10 porcento de aumento
Acima de R$ 100 - 15 porcento de aumento\n
Por favo, digite o valor do seu produto: 
"""))


preco_5 = preco_antigo + (preco_antigo*0.05)
preco_10 = preco_antigo + (preco_antigo*0.10)
preco_15 = preco_antigo + (preco_antigo*0.15)


if preco_antigo < 50:
    print("O valor do produto atualizado é de R$ {}".format(preco_5))
elif preco_antigo >= 50 and preco_antigo < 100:
    print("O valor do produto atualizado é de R$ {}".format(preco_10))
elif preco_antigo > 100:
    print("O valor do produto atualizado é de R$ {}".format(preco_15))

if preco_5 < 80:
    print("Considerado Barato")
elif preco_10 >= 80 and preco_10 < 120:
    print("Considerado Normal")
elif preco_15 >= 120 and preco_15 < 200:
    print("Considerado Caro")
else:
    print("Muito caro")