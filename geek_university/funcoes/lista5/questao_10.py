def maior_numero(num1, num2):
    if num1 > num2:
        return '{} é maior do que {}'.format(num1, num2)
    else:
        return '{} é maio do que {}'.format(num2, num1)

print(maior_numero(4, 6))
print(maior_numero(3, 1))