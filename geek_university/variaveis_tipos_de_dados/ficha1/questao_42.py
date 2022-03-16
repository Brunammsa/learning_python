salario_base = float(input("Digite o salario base do funcionário: "))
gratificacao = salario_base * 0.05
imposto = salario_base *0.07
calculo_final = (salario_base + gratificacao) - imposto

print("ao final o funcionario ira receber com gratificacao e desconto do imposto: {}".format(calculo_final))