apostador1 = int(input("quanto o apostador um investiu? "))
apostador2 = int(input("quanto o apostador dois investiu? "))
apostador3 = int(input("quanto o apostado tres investiu? "))
valor_do_premio = int(input("digite o valor do premio: "))
calculo1 = valor_do_premio + apostador1
calculo2 = valor_do_premio + apostador2
calculo3 = valor_do_premio + apostador3

print("o valor do premio eh de R$ {} e caso o apostador ganhe, ele levara R$ {}".format(valor_do_premio, calculo1))
print("o valor do premio eh de R$ {} e caso o apostador ganhe, ele levara R$ {}".format(valor_do_premio, calculo2))
print("o valor do premio eh de R$ {} e caso o apostador ganhe, ele levara R$ {}".format(valor_do_premio, calculo3))
