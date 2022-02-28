pergunta = int(input('Digite um número: '))
contagem = 0

for i in range(1, pergunta+1):
    numero = int(input('Digite números variados {} vezes:'.format(pergunta)))
    if contagem == 0:
        maior = numero
    if numero > maior:
        maior = numero
print('O maior número entre os valores é o {}'.format(maior))
print('O {} se repetiu {}'.format(maior, ))

#preciso terminar