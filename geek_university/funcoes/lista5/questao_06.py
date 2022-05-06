def numeros_inteiros(num_horas, num_minutos, num_segundos):
    segundos = (num_horas * 60) + (num_minutos * 60) + num_segundos
    return segundos

print(numeros_inteiros(3, 34, 4))