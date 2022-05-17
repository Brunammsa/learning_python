def triangulo(n=6):
    quantidade_de_espacos = n-1
    aux_incremento = 0
    quantidade_de_linhas = (2 * n) - 1
    for i in range(n):
        quantidade_de_asteriscos = quantidade_de_linhas - (2 * quantidade_de_espacos)
        print(quantidade_de_espacos * ' ', (quantidade_de_asteriscos) * '*')
        quantidade_de_espacos -= 1

triangulo(6)