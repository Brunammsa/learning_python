valor_dia = 30.0
dias = int(input("diga o numero de dias trabahados: "))
valor_liquido = valor_dia * dias
valor_com_desconto = valor_liquido * 0.92

print("o valor do salario liquido com desconto eh: R${}".format(valor_com_desconto))