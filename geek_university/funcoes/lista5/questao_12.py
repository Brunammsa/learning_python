# modo 01
def soma_algarismos(numero):
    if numero > 0:
        numero_str = str(numero)
        numeros_separados = []
        for i in numero_str:
            numeros_separados.append(int(i))
        return sum(numeros_separados)
    elif numero < 0:
        return 'número inválido'

print(soma_algarismos(34))

# modo 02
def soma_algarismos(numero):
    if numero > 0:
        numero_str = str(numero)
        numeros_separados = []
        for i in range(len(numero_str)):
            numeros_separados.append(int(numero_str[i]))
        return sum(numeros_separados)
    elif numero < 0:
        return 'número inválido'

print(soma_algarismos(365))

# modo 03
def soma_algorismos_mais_facil(numero):
    if numero > 0:
        soma = 0
        for i in str(numero):
            soma += int(i)
        return soma
    return 0

print(soma_algorismos_mais_facil(365))

# modo 04
def soma_algorismos_mais_facil_ainda(numero):
    if numero <= 0:
        return 0
    soma = 0
    for i in str(numero):
        soma += int(i)
    return soma
print(soma_algorismos_mais_facil_ainda(365))
