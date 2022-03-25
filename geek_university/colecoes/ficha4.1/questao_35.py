numero_a = []
numero_b = []

while len(numero_a) < 1:
    numb1 = int(input('Digite um número >>> '))
    numb2 = int(input('Digite outro número >>> '))
    if numb2 < 0 and numb2 > 10000 or numb2 < 0 and numb2 > 10000:
        print('tente novamente')
    else:
        numero_a.append(numb1)
        numero_b.append(numb2)
    for index, valor in enumerate(numero_a):
        if numero_a[index] < numero_b[index]:
            numero_a.extend(numero_b)
            print(numero_a)
            print(sum(numero_a))
        else:
            numero_b.extend(numero_a)
            print(numero_b)
            print(sum(numero_b))
# agora ta dando certo, mas com um novo erro de out of range ...