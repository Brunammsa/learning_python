
numero_a_ser_testado = 5

def fatorial_exponencial(numero):
    resultado_expo = numero

    for i in range(numero -1, 1, -1):
        resultado_expo = resultado_expo ** i

    return resultado_expo


def fatorial_exponencial_matematicamente(numero):
    potencia = 1

    for i in range(numero -1, 1, -1):
        potencia = potencia * i

    return numero ** potencia


resultado = fatorial_exponencial(numero_a_ser_testado)
print(resultado)

resultado = fatorial_exponencial_matematicamente(numero_a_ser_testado)
print(resultado)
