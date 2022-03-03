while True:
    resistor_1 = int(input('Forneça um valor para a primeira resistência >>> '))
    resistor_2 = int(input('Forneça um valor para a segunda resistência >>> '))
    resistencia = (resistor_1 * resistor_2) / (resistor_1 + resistor_2)
    if resistencia == 0:
        break
    else:
        print('\n *** Tente novamente, a resistência precisa ser igual a zero ***\n')
