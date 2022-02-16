salario = float(input("digite o salário do trabalhador: R$ "))
prestacao_emprestimo = float(input("digite o valor da prestação do empréstimo: R$ "))

porcenta_salario = salario * 0.20

if prestacao_emprestimo > porcenta_salario:
    print("empréstimo não concedido")
else:
    print("empréstimo concedido")