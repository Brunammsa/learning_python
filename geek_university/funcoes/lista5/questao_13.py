def operacao_com_numeros(num1, num2, simbolo):
    if simbolo == '+':
        return num1 + num2
    elif simbolo == '-':
        return num1 - num2
    elif simbolo == '/':
        return num1 / num2

print(operacao_com_numeros(3, 4, '+'))
print(operacao_com_numeros(3, 4, '-'))
print(operacao_com_numeros(3, 4, '/'))