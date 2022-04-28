vetor = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

vetor.sort()
print(vetor)

# o meu castigo por não usar o BubbleSort, vai ser usa-lá como uma função
vetor = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

def bubblesort(lista_desordenada):
    lista = lista_desordenada
    tamanho_da_lista = len(lista)

    for i in range(tamanho_da_lista - 1):
        for j in range(tamanho_da_lista - i - 1):
            if lista[j] > lista[j + 1]:
                elemento_atual = lista[j]
                prox_elemento = lista[j + 1]
                lista[j] = prox_elemento
                lista[j + 1] = elemento_atual
    return lista

lista_ordenada = bubblesort(vetor)
print(lista_ordenada)
