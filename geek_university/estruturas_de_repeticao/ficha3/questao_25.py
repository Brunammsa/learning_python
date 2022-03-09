soma_multiplos_de_3 = 0
soma_multiplos_de_5 = 0
soma_dos_multiplos_3_5 = 0

valor = 1

while valor < 1000:
    multiplicacao = 1000 * valor
    if multiplicacao % 3 == 0:
        soma_multiplos_de_3 += 1
    if multiplicacao % 5 == 0:
        soma_multiplos_de_5 += 1
    valor += 1
    
soma_dos_multiplos_3_5 = soma_multiplos_de_3 + soma_multiplos_de_5
print('A soma dos múltiplos de 3 e 5 até o número 1000 é {}'.format(soma_dos_multiplos_3_5))
