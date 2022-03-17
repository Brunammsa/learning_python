soma_dos_primos = 0
quantidade_divisores = 0
numero = 2

while numero < 2000000: # é muito grande, trava meu pc, mas ta correto
    for i in range(1, numero + 1):
        if numero % i == 0:
            quantidade_divisores += 1
    if quantidade_divisores == 2:
        soma_dos_primos += numero
    numero += 1
    quantidade_divisores = 0
print('A soma dos números primos é {}'.format(soma_dos_primos))
