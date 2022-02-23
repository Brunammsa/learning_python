salario_atual = float(input("Digite o valor do salário atual do funcionário: R$ "))
tempo_servico = int(input("Digite o tempo de serviço do funcionário em anos: "))

if salario_atual < 500 and tempo_servico < 1:
    print("O funcionário receberá 25 porcento de reajuste ficando R$ {} e não ganhará bônos por tempo de serviço".format(salario_atual + (salario_atual*0.25)))
elif salario_atual >= 500 and salario_atual < 1000 and tempo_servico > 1 and tempo_servico < 3:
    print("O funcionário receberá 20 porcento de reajuste e ganhará bônos por tempo de serviço, ficando o total de R$ {}".format(salario_atual + (salario_atual*0.20) + 100))
elif salario_atual >= 1000 and salario_atual < 1500 and tempo_servico > 4 and tempo_servico < 6:
    print("O funcionário receberá 15 porcento de reajuste e ganhará bônos por tempo de serviço, ficando o total de R$ {}".format(salario_atual + (salario_atual*0.15) + 200))
elif salario_atual >= 1500 and salario_atual < 2000 and tempo_servico > 7 and tempo_servico < 10:
    print("O funcionário receberá 10 porcento de reajuste e ganhará bônos por tempo de serviço, ficando o total de R$ {}".format(salario_atual + (salario_atual*0.10) + 300))
elif salario_atual > 2000 and tempo_servico > 10:
    print("O funcionário não receberá reajuste mas ganhará bônos por tempo de serviço, ficando o total de R$ {}".format(salario_atual + 500))
else:
    print("informações inválidas, tente novamente o que se pede")


