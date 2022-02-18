nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media_notas = float(nota1+nota2)/2

if nota1 < 0 :
    print("Nota inválida, tente entre 0 e 10")
elif nota1 > 10:
    print("Nota inválida, tente entre 0 e 10")
elif nota2 < 0:
        print("Nota inválida, tente entre 0 e 10")
elif nota2 > 10:
        print("Nota inválida, tente entre 0 e 10")
else:
    print("A média entre as notas {} e {} é {}".format(nota1, nota2, media_notas))  
