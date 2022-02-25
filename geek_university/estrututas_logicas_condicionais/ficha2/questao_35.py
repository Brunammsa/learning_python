import sys

def eh_bissexto(ano):
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return True
    else:
        return False

dia = int(input("Digite uma dia: "))

if dia <= 0 or dia >= 32:
    print("Dia inválido, tente novamente")
    sys.exit()
    
mes = int(input("Digite um mês: "))

if mes <= 0 or mes >= 13:
    print("Este mês é inválido, tente novamente")
    sys.exit()

ano = int(input("Digite um ano: "))

if ano <= 0:
    print("Este ano é inválido, tente novamente")
    sys.exit()


if (mes == 1 or mes == 3 or mes == 7 or mes == 8 or mes == 12) and dia > 31:
    print("Esta data é inválido, tente novamente")
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    print("Esta data é inválido, tente novamente")
elif mes == 2 and not eh_bissexto(ano) and dia > 28:
    print("Esta data é inválida")
elif mes == 2 and eh_bissexto(ano) and dia > 29:
    print("Esta data é invalida")
else:
    print("A data é válida")
