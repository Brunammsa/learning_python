lista_teste = [115, 23, 55, 90, 7]

def vetor_normal(numeros):
    for num in numeros:
        print(num)


def funcao_inversa(vetor):
#   limite = len(vetor)-1
#   for i in range(limite, -1, -1):
#        print(vetor[i])
    for num in reversed(vetor):
        print(num)


def vetor_media(numeros):
    media_aritimetica = sum(numeros)/len(numeros)
    return media_aritimetica


vetor_normal(lista_teste)
funcao_inversa(lista_teste)
print(vetor_media(lista_teste))
