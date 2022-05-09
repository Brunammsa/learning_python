def soma_numeros(num1, num2):
    if num1 > 0 and num2 > 0:
        if num1 < num2:
            soma1 = 0 
            for i in range(num1, num2 + 1):
                soma1 = soma1 + i
            return soma1
        elif num2 < num1:
            soma2 = 0
            for i in range(num2, num1 + 1):
                soma2 = soma2 + i
            return soma2

print(soma_numeros(3, 7))
print(soma_numeros(7, 3))
