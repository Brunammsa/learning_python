def primos(inicio_sequencia, final_sequencia):
    quantidade_divisores = 0
    soma_primos = 0
    while inicio_sequencia < final_sequencia:
        for i in range(1, inicio_sequencia + 1):
            if inicio_sequencia % i == 0:
                quantidade_divisores += 1
        if quantidade_divisores == 2:
            soma_primos += 1
        inicio_sequencia += 1
        quantidade_divisores = 0
    return soma_primos

print(primos(1, 10))
