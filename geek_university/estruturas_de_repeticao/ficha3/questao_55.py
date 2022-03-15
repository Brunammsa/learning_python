resposta = ''
soma_dos_primos = 0
soma_dos_divisores = 0
numero = 2
while resposta != 'sair':
    n = int(input('Quantos números deseja ter na sequência? >>> '))
    if n <= 1:
        print('Número indisponível, tente um positivo')
    else:
        while numero <= n:
            for i in range(numero, n + 1):
                if numero % i == 0:
                    soma_dos_divisores += 1
                    if soma_dos_divisores == 2:
                        soma_dos_primos += numero
            numero += 1
        print('A soma dos números primos é {}'.format(soma_dos_primos))
        resposta = input('Se deseja tentar com outro número aperte "enter", se não, digite "sair" ')
        
# algo de errado não está certo...