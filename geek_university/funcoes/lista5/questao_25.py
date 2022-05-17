def serie(n):
    resultado_serie = 0
    for i in range(1, n + 1):
        s = ((i ** 2) + 1) / (i + 3)
        resultado_serie = resultado_serie + s
    return resultado_serie

print(serie(4))
