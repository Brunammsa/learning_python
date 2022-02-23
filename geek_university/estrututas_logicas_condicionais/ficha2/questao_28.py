x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

geometrica = round((x * y * z) ** 1 / 3,2)
ponderada = round((x + (2*y) + (3 * z)) / 6,2)
harmonica =  round(1 / (1/x + 1/y+ 1/z),2)
aritimetica = round((x + y + z) /3,2)

if x > 0 and y > 0 and z > 0:
    print("Geométrica {}".format(geometrica))
    print("Ponderada {}".format(ponderada))
    print("Harmônica {}".format(harmonica))
    print("Aritimtica {}".format(aritimetica))
