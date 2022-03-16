valores = []

for numeros in range(5):
    num = int(input('Digite 5 números >>> '))
    valores.append(num)
print('o maior valor encontra-se na posição {}'.format(valores.index(max(valores))))
print('o menor valor encontra-se na posicção {}'.format(valores.index(min(valores))))