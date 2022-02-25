import sys
import math

variavel_a = int(input("Digite um valor para a variável a: "))

if variavel_a == 0:
    print("Não é equação de 2º grau")
    sys.exit()

variavel_b = int(input("Digite um valor para a variável b: "))
variavel_c = int(input("Digite um valor para a variável c: "))

calculo_delta = (variavel_b ** 2) - (4*variavel_a*variavel_c)
primeira_raiz = (- variavel_b - math.sqrt(calculo_delta)) / 2 * variavel_a
segunda_raiz = (- variavel_b + math.sqrt(calculo_delta)) / 2 * variavel_a

if calculo_delta < 0:
    print("Não existe raiz")
elif calculo_delta == 0:
    print("Raiz única: {}".format(primeira_raiz))
else:
    print("{} e {}".format(primeira_raiz, segunda_raiz)) 

# 2x² + 4x – 6 = 0
# ax² + bx + c = 0