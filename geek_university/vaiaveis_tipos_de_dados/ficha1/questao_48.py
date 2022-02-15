segundos = int(input("digite um número de segundos: "))
hora = (segundos // 3600)
minutos = (segundos % 3600) // 60
seg_final = (segundos % 3600) % 60

print("{} horas, {} minutos e {} segundos".format(hora, minutos, seg_final))