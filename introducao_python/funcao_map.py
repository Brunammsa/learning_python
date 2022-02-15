def dobro(x):
    return x*2
valor = 2
print(dobro(valor))

# meio enrolado, ele pega do print e joga p def p definir o dobro(x)
# assim é só p 01 unico valor

def dobro(x):
    return x*2

valor2 = [2, 3, 4, 5, 6]

# print(map(dobro, valor2)) assim da erro

valor_dobrado = map(dobro, valor2)

for i in valor_dobrado:
    print(i) #um embaixo do outro

valor_dobrado2 = list(valor2)
print(valor_dobrado2)