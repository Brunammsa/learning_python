saque = int(input('Qual valor deseja sacar? >>> R$ '))

quantidade_de_cedulas = 0
cedula = 100 #com
total_do_saque = saque

while True:
    if total_do_saque >= cedula:
        total_do_saque -= cedula
        quantidade_de_cedulas += 1
    else:
        print('{} cedulas de {} reais'.format(quantidade_de_cedulas, cedula))
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        quantidade_de_cedulas = 0
        if total_do_saque == 0:
            break
# Complicada, mas entendi