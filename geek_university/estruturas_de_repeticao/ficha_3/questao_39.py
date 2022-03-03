base_do_triangulo = int(input('Digite um valor para a base do triângulo >>> '))
altura_do_triangulo = int(input('Digite um valor para a altura do triangulo >>> '))

calculo_area_triangulo = (base_do_triangulo * altura_do_triangulo) / 2

if base_do_triangulo <= 0 or altura_do_triangulo <= 0:
    print('Dados inválidos, tente novamente')
else:
    print('A área do triângulo é {}'. format(calculo_area_triangulo))

# Não imagino um modo mais fácil p fazer se não assim.