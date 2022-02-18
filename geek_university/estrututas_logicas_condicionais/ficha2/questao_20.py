lado_a = int(input("Digite o valor do lado A do triângulo: "))
lado_b = int(input("Digite o valor do lado B do triângulo: "))
lado_c = int(input("Digite o valor do lado C do triângulo: "))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_b + lado_a:
    print("Temos um triângulo ")
    if lado_a == lado_b == lado_c:
        print("Equilátero")
    elif lado_a != lado_b != lado_c != lado_a:
        print("Escaleno")
    else:
        print("Isóceles")
else:
    print("Os valores dados não formam triângulo")