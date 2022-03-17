a = int(input('Digite o início da sequência >>> '))
b = int(input('Digite o final da sequência >>> '))

soma_primos = 0
quantidade_divisores = 0

while a < b:
    for i in range(1, a + 1):
        if a % i == 0:
            quantidade_divisores += 1
    if quantidade_divisores == 2:
        soma_primos += a
    a += 1
    quantidade_divisores = 0
print('A soma entre os primos de "a" e "b" é de {}'.format(soma_primos))
