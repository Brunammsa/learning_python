soma = 0

for valores in range(10, 20):
    numero = int(input('Digite {} notas >>> '.format(valores)))
    if numero < 10 or numero > 20:
        print('Insira uma nota válida de aprovação')
    else:
        soma += numero
    print(round(soma/valores,2))
