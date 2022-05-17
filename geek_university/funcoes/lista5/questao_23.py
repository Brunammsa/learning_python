def triangulo_lateral_return(n=4):
    aux_decremento = 0
    quantidade_de_linhas = (2 * n) - 1
    for i in range(quantidade_de_linhas):
        if i+1 > n:
            aux_decremento = quantidade_de_linhas - i
            print(aux_decremento * '*')
        else:
            print((i + 1) * '*')

triangulo_lateral_return(4)
