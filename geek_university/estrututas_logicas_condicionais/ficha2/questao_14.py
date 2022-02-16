nota_laboratorio = float(input("Digite a nota do laboratório: "))
nota_avaliacao_semestral = float(input("Digite a nota da avaliação semestral: "))
nota_exame_final = float(input("Digite a nota do exame final: "))

peso_laboratório = int(input("Digite o peso da nota do laboratório: "))
peso_avaliacao = int(input("Digite o peso da avaliação: "))
peso_exame = int(input("Digite o peso do exame final: "))

reprovado = [:2.9] # Não to sabendo
recuperacao = [3:4.9]# Não to sabendo
media_ponderada = (nota_laboratorio*peso_laboratório + nota_avaliacao_semestral*peso_avaliacao + nota_exame_final*peso_exame) / (peso_exame+peso_avaliacao+peso_laboratório)

if float(media_ponderada) == reprovado:
    print("Aluno reprovado")
elif float(media_ponderada) == recuperacao:
    print("Aluno de recuperação")
else:
    print("Aluno aprovado")
