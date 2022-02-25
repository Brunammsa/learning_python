ano = int(input("Digite um ano e descubra se ele é bissexto ou não: "))

def eh_bissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return True
    else:
        return False

if eh_bissexto(ano):
    print("Este ano é bissexto")
else:
    print("Este ano não é ")
