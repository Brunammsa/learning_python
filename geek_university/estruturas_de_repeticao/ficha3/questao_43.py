lista_de_idades = 0
soma = 0


while True:
    comando = int(input('Digite uma idade por vez >>> '))
    soma += 1
    lista_de_idades = comando + lista_de_idades
    media_das_idades = lista_de_idades/soma
    if comando == 0:
        break
    else:
        print('A média das idades é de {}'.format(round(media_das_idades,2)))
