def numeros_pares_do_vetor(numero):
    contagem_pares = 0
    for i in numero:
        if i %2 == 0:
            contagem_pares += 1
    return contagem_pares

lista = [1, 2, 3, 4, 5]
print(numeros_pares_do_vetor(lista))