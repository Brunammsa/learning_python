a = int(input('Digite um valor para o início da sequência >>> '))
b = int(input('Digite um valor para o final da sequência >>> '))

quantidade_de_divisores = 0
quantidade_de_primos = []

while a < b:
    for i in range(1, a + 1):
        if a % i == 0:
            quantidade_de_divisores += 1
    if quantidade_de_divisores == 2:
        quantidade_de_primos.append(a)
    a += 1
    quantidade_de_divisores = 0
print('A quantidade de primos entre "a" e "b" "é de {}'.format(len(quantidade_de_primos)))