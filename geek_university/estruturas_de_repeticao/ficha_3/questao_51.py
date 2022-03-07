salario_inicial = 2000
primeiro_aumento = salario_inicial * (1.5/100)
primeiro_ano_de_reajuste = 1996

ano_atual = int(input('Digite o último ano trabalhado para saber o último reajuste >>> '))


while primeiro_ano_de_reajuste <= ano_atual:
    primeiro_ano_de_reajuste += 1
    salario_inicial = salario_inicial + primeiro_aumento
    primeiro_aumento *= 2
    print('O salário no ano de {} será de R$ {}'.format(primeiro_ano_de_reajuste, salario_inicial))
