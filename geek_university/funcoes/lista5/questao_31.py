def fatorial(numero):
    auxiliar = 1
    for i in range(numero, 0, - 1):
        auxiliar *= i
    return auxiliar

def numero(n):
    somatorio = 0
    for i in range(0, n + 1):
        somatorio += 1/fatorial(i)
    return somatorio

print(numero(5))
