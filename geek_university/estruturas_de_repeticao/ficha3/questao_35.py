valor_inicial_intervalo = int(input('Digite um valor para o início do intervalo >>> '))
valor_final_intervalo = int(input('Digite um valor para o final do intervalo >>> '))

soma = 0

if valor_inicial_intervalo > valor_final_intervalo:
    print('Intervalo de valores inválidos')
else:
    for i in range(valor_inicial_intervalo, valor_final_intervalo+1):
        if i %2 != 0:
            soma += i
    print('Soma dos ímpares neste intervalo: {}'.format(soma))