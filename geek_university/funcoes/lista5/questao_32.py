# 36/60 - 18/30 - 9/15 - 3/5 

def simplifica(numerador, denominador):
    numerador_simplificado = numerador
    denominador_simplificado = denominador

    if numerador < denominador:
        menor_numero = numerador
    else:
        menor_numero = denominador

    i = 2
    n = 1
    while n < menor_numero:
        if numerador_simplificado % i == 0 and denominador_simplificado % i == 0:
            numerador_simplificado = numerador_simplificado / i
            denominador_simplificado = denominador_simplificado / i
            i = 2
        else:
            i += 1
        n += 1
        
    return numerador_simplificado, denominador_simplificado

a,b = simplifica(36, 60) 
print(a)
print(b)