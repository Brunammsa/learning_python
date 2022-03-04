from os import _T1


quantidade_de_termos = int(input('Digite a quantidade de termos para a sequêcia de Fibonacci >>> '))

t1 = 0
t2 = 1
contador = 3
soma = 0

while contador < quantidade_de_termos:
    t3 = t1+t2
    t1 = t2
    t2 = t3
    for i in range(t1, t3, 2):
        soma += 1
    while range(t1, t3) < 4000000 :
        contador += 1
# Não estou acertando fazer, voltar para esta questão mais tarde