from sys import exc_info


nota_alunos = float(input("Digite a nota do aluno: "))
faltas_alunos = int(input("Digite o número de falta do aluno: "))

if nota_alunos >= 9 and nota_alunos <= 10 and faltas_alunos <= 20:
    print("Conceito A")
elif nota_alunos >= 9 and nota_alunos <= 10 and faltas_alunos > 20:
    print("Conceito B")
elif nota_alunos >= 7.5 and nota_alunos <=8.9 and faltas_alunos <= 20:
    print("Conceito B")
elif nota_alunos >= 7.5 and nota_alunos <=8.9 and faltas_alunos > 20:
    print("Conceito C")
elif nota_alunos >= 5 and nota_alunos <= 7.4 and faltas_alunos <= 20:
    print("Conceito C")
elif nota_alunos >= 5 and nota_alunos <= 7.4 and faltas_alunos > 20:
    print("Conceito D")
elif nota_alunos >= 4 and nota_alunos <= 4.9 and faltas_alunos <= 20:
    print("Conceito D")
elif nota_alunos >= 4 and nota_alunos <= 4.9 and faltas_alunos > 20:
    print("Conceito E")
elif nota_alunos >= 0 and nota_alunos <= 3.9 and faltas_alunos <= 20:
    print("Conceito E")
elif nota_alunos >= 0 and nota_alunos <= 3.9 and faltas_alunos > 20:
    print("Conceito E")
else:
    print("Valores indisponíveis")
