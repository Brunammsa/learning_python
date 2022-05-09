def triangulo(lado1, lado2, lado3):
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
        if lado1 == lado2 == lado3:
            return "Temos um triângulo, ele é equilátero"
        elif lado1 != lado2 != lado3 != lado1:
            return "Temos um triângulo, ele é escaleno"
        else:
            return "Temos um triângulo, ele é isóceles"
print(triangulo(6, 10, 7))