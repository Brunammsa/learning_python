preco_produto = float(input("""
escolha um valor entre a tabela abaixo e veja quanto fica com o reajuste.
Preço antigo / aumento de:
Até 50 reais - 5%
entre 50 reais e 100 reais - 10%
acima de 100 reais - 15%
"""))

preco_5 = preco_produto * 0.05 + preco_produto
preco_10 = preco_produto * 0.10 + preco_produto
preco_15 = preco_produto * 0.15 + preco_produto

if (preco_produto <= 50) + preco_5 and <= 80:
    print("Com o reajuste, seu valor final ficou R$ {}, considerando-se barato".format(preco_produto+preco_5))

#complicada