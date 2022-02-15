#exemplo 01

x = [1, 2, 3, 4, 5]
y = []

for numeros in x:
    y.append(numeros ** 2) #elevado ao quadrado **
print(x)
print(y)

#obs1: o que foi feito? elevei ao quadrado cada elemento dentro da variavel x e adicionei seu resultado na variavel y

#exemplo 02

a = [1, 2, 3, 4, 5]
b = [numeros ** 2 for numeros in a] # [valor_a adc laço condicao] (esse ex não tem condicao)
print(a)
print(b)

#com condicao

c = [1, 2, 3, 4, 5]
d = [numeros for numeros in c if numeros % 2 == 1]
print(d)

#pegar os numeros da lista c que tenham restos 1 (impares)