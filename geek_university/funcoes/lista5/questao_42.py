def media_do_vetor(numeros):
    quantidade_de_numeros = 0
    soma_dos_numeros = 0
    for i in numeros:
        quantidade_de_numeros += 1
        soma_dos_numeros += i
    media = soma_dos_numeros/quantidade_de_numeros
    return media

lista = [1, 2, 3, 4, 5]
print(media_do_vetor(lista))