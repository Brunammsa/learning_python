quantidade = int(input("Quantas vezes rodar o loop? "))
soma = 0

for i in range(1,quantidade+1):
    numero = int(input("Digite um valor qualquer 10x: "))
    soma = soma + numero
print("A soma dos valores do loop é {}".format(soma))