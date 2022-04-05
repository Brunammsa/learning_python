numero_a = []
numero_b = []

while len(numero_a) < 1:
    numb1 = int(input('Digite um número >>> '))
    numb2 = int(input('Digite outro número >>> '))
    if numb1 < 0 or numb1 > 10000 or numb2 < 0 or numb2 > 10000:
        print('tente novamente')
    else:
        numero_a.append(numb1)
        numero_b.append(numb2)
    
for i in range(1):
    if numero_a[i] < numero_b[i]:
        numero_a.extend(numero_b)
        print(numero_a)
        print(sum(numero_a))
    else:
        numero_b.extend(numero_a)
        print(numero_b)
        print(sum(numero_b))
