altura = float(input("Digite a sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / altura ** 2

if imc < 18.5:
    print("Abaixo do peso")
elif imc > 18.6 and imc < 24.9:
    print("Saudável")
elif imc > 25 and imc < 29.9:
    print("Peso em excesso")
elif imc > 30 and imc < 34.9:
    print("Obesidade Grau I")
elif imc > 35 and imc < 39.9:
    print("Obesidde Grau II (Severa)")
elif imc >= 40:
    print("Obesidad Gray III (Mórbida)")