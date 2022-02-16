nota_1 = float(input("digite a nota da primeira prova: "))
nota_2 = float(input("digite a nota da segunda prova: "))
nota_3 = float(input("digite a nota da terceira prova: "))
peso_1 = int(input("Digite o peso da primeira e segunda prova: "))
peso_2 = int(input("Digite o peso da terceira nota: "))

media_ponderada = (nota_1 * peso_1 + nota_2 * peso_1 + nota_3 * peso_2) / (peso_1 + peso_2)

if float(media_ponderada) >= 60:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")