pergunta = int(input('Digite o número de repetições >>> '))
quantidade_x_numero_digitado = 0

for _ in range(1, pergunta+1):
    numero = int(input('Digite um número >>> '))
    if quantidade_x_numero_digitado == 0:
        maior = numero
    if numero > maior:
        quantidade_x_numero_digitado += 1
        maior = numero
    if numero != maior:
        quantidade_x_numero_digitado = 1
print('Maior número é o {} e se repetiu {} vezes'.format(maior, quantidade_x_numero_digitado))
#refazer parte de cima

pergunta = int(input('Digite um número: '))
valor = 0
lista_maior_numero = []

while valor < pergunta:
    numero = int(input('Digite números variados {} vezs: '.format(pergunta)))
    valor += 1
    lista_maior_numero.append(numero)

maior = max(lista_maior_numero)
maior_numero_repeticao = lista_maior_numero.count(maior)

print('O maior valor entre os números digitados é o {} e foi repetido {} vezes'.format(maior, maior_numero_repeticao))
