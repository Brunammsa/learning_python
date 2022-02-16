nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media_notas = float(nota1+nota2)/2

if nota1 and nota2 > 0.0:
    print("as notas são válidas e sua média é {}".format(media_notas))
else:
    print("tem nota inválida, não é possível gerar a média do aluno")
