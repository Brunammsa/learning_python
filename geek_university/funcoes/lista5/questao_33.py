def soma_algarismos(n):
    fatorial = 1
    for i in range(n, 0, -1):
        fatorial = fatorial * i
    fatorial_str = str(fatorial)
    soma_fatorial = 0
    for i in fatorial_str:
        soma_fatorial = soma_fatorial + int(i)
    return soma_fatorial

print(soma_algarismos(4))
