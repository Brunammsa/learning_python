import datetime
import random


def data_de_hoje():
    hoje = datetime.datetime.now()
    return str(hoje.day) + "-" + str(hoje.month) + "-" + str(hoje.year)


numeros_da_sorte = ""
for i in range(7):
    numero_aleatorio = random.randint(0, 10)
    numeros_da_sorte += str(numero_aleatorio) + " "


texto_do_sorteio = "Os números da sorte de " + data_de_hoje() + " são:"
print(texto_do_sorteio)
print(numeros_da_sorte)

file = open("sorteio.txt", "w")
file.write(texto_do_sorteio)
file.write("\n")
file.write(numeros_da_sorte)

file.close()