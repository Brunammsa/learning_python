idade = int(input("Por favor, digite a idade do trabalhador: "))
tempo_servico = float(input("Por favor, digite o tempo de serviço do trabalhador: "))

if idade >= 65:
    print("O trabalhador já tem idade para se aposentar")
elif tempo_servico >= 30:
    print("O trabalhador já tem tempo de serviço suficiente para se aposentar")
elif idade >= 60 and tempo_servico >= 25:
    print("O trabalhador já tem idade mais tempo de serviço juntos para se aposentar")
else:
    print("Ou o trabalhador não possui idade e/ou tempo de serviço suficientes para se aposentar")