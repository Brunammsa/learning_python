soma = 0

for i in range(1, 11):
    numero = int(input("Digite um valor 10x: "))
    if numero > 0:
        soma = soma + numero
print("A média dos valores digitados é de {}".format(soma / 10))

