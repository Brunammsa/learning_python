quantidade_limite_multiplos = int(input('Leia um valor inteiro e positivo para "n" >>> '))
i = int(input('Leia um valor inteiro e positivo para "i" >>> '))
j = int(input('Leia um valor inteiro e positivo para "j" >>> '))

multiplos_encontrados = 0
numero = 0

if quantidade_limite_multiplos < 0 or i < 0 or j < 0:
    print('Valores inválidos, tente novamente')
else:
    while multiplos_encontrados < quantidade_limite_multiplos:
        if numero % i == 0 or numero % j == 0:
            multiplos_encontrados += 1
            print(numero)
        numero += 1
        