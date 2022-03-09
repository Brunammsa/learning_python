lista_de_numeros = []

while True:
    comando = int(input('Digite um número inteiro >>> '))
    if comando < 0:
        break
    else:
        lista_de_numeros.append(comando)
    
maior_numero = max(lista_de_numeros)
menor_numero = min(lista_de_numeros)

print('O maior e o menor número respectivamente foram os {} e {}'.format(maior_numero, menor_numero))