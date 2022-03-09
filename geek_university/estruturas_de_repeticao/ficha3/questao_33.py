n = int(input('Digite o limite de termos >>> '))
i = int(input('Dê valor ao i >>> '))
j = int(input('Dê valor ao j >>> '))

valor = 0
numeros_multiplos = 0

if i %2 != 0 or j %2 != 0:
    print('Números inválidos, tente inteiros positivos')

while numeros_multiplos < n:
    if valor % i == 0 or valor % j == 0:
        numeros_multiplos += 1
        print(valor)
    valor += 1
