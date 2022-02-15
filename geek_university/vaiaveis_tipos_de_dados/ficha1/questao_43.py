valor_qualquer = float(input("digite um valor qualquer: "))
valor_com_desconto = valor_qualquer * 0.90
valor_parcelado = valor_qualquer / 3
comissao_vendedor_a_vista = valor_com_desconto * 0.05
comissao_vendedor_parcelado = valor_parcelado *0.05

print("o valor com 10 por centa de desconto eh {}, o valor de cada parcela dividido em 3x eh {}, a comissao do vendedor em cima do valor a vista eh {} e a comissao do vendedor sobre o valor parcelado eh {}".format(valor_com_desconto, valor_parcelado, comissao_vendedor_a_vista, comissao_vendedor_parcelado))
