def quadrado_perfeito(numero):
    raiz_quadrada = (numero ** (1/2))
    if (raiz_quadrada ** 2) == numero:
        return 'É quadrado perfeito'
    else:
        return 'Não é quadrado perfeito'

print(quadrado_perfeito(2))
print(quadrado_perfeito(9))
