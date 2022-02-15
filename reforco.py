import random

#random.seed(1)
numero = random.randint(0,20)
print(numero)

numero = random.randint(2,6)
print(numero)

numeros = [3, 5, 6, 1]
numero_sorteado = random.choice(numeros)
print(numero_sorteado)

from datetime import date
data_de_hoje = date.today()
print(data_de_hoje) #vai sair no estilo americano ANSI

data_em_texto = "{}/{}/{}".format(data_de_hoje.day, data_de_hoje.month, data_de_hoje.year)
print(data_em_texto) #transformando em string a data em br

data_em_texto = data_de_hoje.strftime("%d/%m/%Y") #isso coloca os 0 qnd for tipo dia 2 e não atrapalha qnd for dia 10 por ex.
print(data_em_texto)

from datetime import datetime

data_e_hora_atual = datetime.now()
data_em_texto = data_e_hora_atual.strftime("%d/%m/%Y %H:%M")
print(data_em_texto)

data_em_texto = "02/02/2022 17:48"
data_e_hora_atual = datetime.strptime(data_em_texto, "%d/%m/%Y %H:%M")
print(data_e_hora_atual) #não entendi a diferença do transformar em string


print(type(data_e_hora_atual))