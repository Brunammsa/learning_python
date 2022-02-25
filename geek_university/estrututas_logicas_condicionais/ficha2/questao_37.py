import sys
"""
1ª e 2ª hora - R$ 1,00 cada
3ª e 4ª hora - R$ 1,40 cada
5ª hora e seguintes - R$ 2,00 cada
"""

hora_entrada = int(input("Digite a hora de entrada: "))
min_entrada = int(input("Digite a minuto de saída: "))
hora_saida = int(input("Digite a hora de entrada: "))
min_saida = int(input("Digite a minuto de saída: "))

if (hora_entrada < 0 or hora_entrada >= 23) or (hora_saida < 0 or hora_saida >= 23):
    print("Hora inválida, tente novamente")
    sys.exit()
if (min_entrada < 0 or min_entrada >= 60) or (min_saida < 0 or min_saida >= 60):
    print("Minuto inválido, tent novamente")
    sys.exit()

if hora_entrada > hora_saida:
    hora_final = (hora_saida + 24) - hora_entrada
else:
    hora_final = hora_saida - hora_entrada

if min_entrada > min_saida:
    min_final = (min_saida + 60) - min_entrada
else:
    min_final = min_saida - min_entrada

print("A permanência foi de {} horas e {} minutos".format(hora_final, min_final))

tempo_final_em_minutos = (hora_final * 60) + min_final

if tempo_final_em_minutos >= 1  and tempo_final_em_minutos <= 60:
    print("O valor do estacionamento será R$ 1,00")
elif tempo_final_em_minutos > 60 and tempo_final_em_minutos <= 120:
    print("O valor do estacionamento será R$ 2,00")
elif tempo_final_em_minutos > 120 and tempo_final_em_minutos <= 180:
    print("O valor do estacionamento será R$ 4,20")
elif tempo_final_em_minutos > 180 and tempo_final_em_minutos <= 240:
    print("O valor do estacionamento será R$ 5,60")
elif tempo_final_em_minutos > 240:
    print("O valor do estacionamento será R$ {}".format(hora_final * 2))
else:
    print("Tempo limite, não precisa pagar")
