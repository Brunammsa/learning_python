contagem = 0

while contagem < 10:
    numero = int(input('Digite um número inteiro 10 vezes: '))
    if contagem == 0:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    contagem = contagem + 1
print('O menor número é o {} e o maior é o {}'.format(menor, maior))
