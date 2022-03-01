numero_digitado = input('Digite um número de 100 a 999: ')

if int(numero_digitado) < 100 or int(numero_digitado) > 999:
    print('Valor inválido, digite novamente um inteiro entre 100 e 999')
else:
    for numero in numero_digitado:
        print(numero)

#outra abordagem

numero_digitado = input('Digite um número de 100 a 999: ')

if len(numero_digitado) != 3:
    print('Valor inválido, digite novamente um inteiro entre 100 e 999')
else:
    for numero in numero_digitado:
        print(numero)