numero_a = int(input('Digite um número inteiro com 3 digitos >>> '))
numero_b = int(input('Digite outro número inteiro com 3 digitos >>> '))

calculo = numero_a * numero_b

if str(len(numero_a)) != 3 or str(len(numero_b)) != 3:
    print('É necessário um número com 3 digitos')

print('O resultado dos números digitados é {}'.format(int(calculo)))
# Errada