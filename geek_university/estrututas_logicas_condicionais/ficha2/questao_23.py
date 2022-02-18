ano = int(input("Digite um ano e descubra se ele é bissexto ou não: "))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print("Este ano é bissexto")
else:
    print("Este ano não é bissexto")