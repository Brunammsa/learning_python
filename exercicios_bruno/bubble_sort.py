lista = [95, 9, 60, 61, 89, 34, 25]
tamanho_da_lista = len(lista)

for i in range(tamanho_da_lista - 1):
    for j in range(tamanho_da_lista - i - 1):
        if lista[j] < lista[j + 1]:
            elemento_atual = lista[j]
            prox_elemento = lista[j + 1]
            lista[j] = prox_elemento
            lista[j + 1] = elemento_atual
print(lista)

#A  P
[3, 2, 1]

#   A  P
[2, 3, 1]

#      A
[2, 1, 3]

#A  P
[2, 1, 3]

#   A  
[1, 2, 3]