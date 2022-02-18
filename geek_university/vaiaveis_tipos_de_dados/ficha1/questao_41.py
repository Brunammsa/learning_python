valor_hora_trabalhada = float(input("digite o valor da hora trabalhada: "))
numero_horas_trabalhadas = float(input("digite o numero de horas trabalhadas: "))
adicional =valor_hora_trabalhada * 0.10
valor_final = (valor_hora_trabalhada * numero_horas_trabalhadas) + adicional

print("o valor da hora trabalhada por {} dias com acrescimo de 10 porcento foi: {}".format(numero_horas_trabalhadas, valor_final))
