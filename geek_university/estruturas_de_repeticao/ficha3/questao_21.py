inico_intervalo = int(input('Digite o início do intervalo >>> '))
limite_intervalo = int(input('Digite o limite do intervalo >>> '))

soma = 0
multiplicacao = 1

for numero in range(inico_intervalo, limite_intervalo+1):
    if numero %2 == 0:
        soma += numero
    if numero %2 != 0:
        multiplicacao *= numero
print(soma)
print(multiplicacao)
