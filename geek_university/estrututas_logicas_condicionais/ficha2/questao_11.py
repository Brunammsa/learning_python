numero_digitado = input("Digite um número inteiro maior do que zero: ")
acumulador = 0

if int(numero_digitado) < 0:
    print("Número inválido")
else:
    for digito in numero_digitado:
        acumulador += int(digito)
    print(acumulador)
