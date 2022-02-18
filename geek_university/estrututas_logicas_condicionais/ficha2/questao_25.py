variavel_a = int(input("Digite um valor para a variável a: "))
variavel_b = int(input("Digite um valor para a variável b: "))
variavel_c = int(input("Digite um valor para a variável c: "))

calculo_delta = (variavel_b ** 2) - (4*variavel_a*variavel_c)

if calculo_delta < 0:
    print("Não exist raiz")
elif calculo_delta == 0:
    print("Ráiz única")
elif calculo_delta >= 0:
    print("") 

#não to sacando muito bem como faz.. ta bem incompleta e talvez errada também (parte feita)
