idade_nadador = int(input("Digite a idade do nadador(a): "))

if idade_nadador >= 5 and idade_nadador <= 7:
    print("Sua categoria é a Infantil A")
elif idade_nadador >= 8 and idade_nadador <= 10:
    print("Sua categoria é a Infantil B")
elif idade_nadador >= 11 and idade_nadador <= 13:
    print("Sua categoria é a Juvenil A")
elif idade_nadador >= 14 and idade_nadador <= 17:
    print("Sua categoria é a Juvenil B")
elif idade_nadador >= 18:
    print("Sênio")
else:
    print("Valores indisponíveis, por favor, tente novamente")
