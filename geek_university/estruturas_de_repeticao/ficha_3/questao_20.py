quantidade_numeros_digitados = 0
quantidade_numeros_pares = 0

while True:
    numero = int(input('Digite um número >>> '))
    if numero == 1000:
        break
    if numero %2 == 0:
        print('Par')
        quantidade_numeros_pares += 1
    quantidade_numeros_digitados += 1
print('{}numeros pares, {} digitados'.format(quantidade_numeros_pares, quantidade_numeros_digitados))
   