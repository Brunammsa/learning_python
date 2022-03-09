numero = int(input('Digite um número >>> '))
total = 0

for termos in range(1, numero + 1):
    if numero <= 1:
        print('Número inválido, digite um número maior do que 1')
    if numero % termos == 0:
        total += 1

if total > 2:
    print('Não é primo')
elif total >= 2:
    print('É primo')
