pergunta = int(input('Digite um número: '))
soma = 0

for i in range(1, pergunta,2):
    soma = soma + i
print("a soma dos 50 primeiros pares é de {}".format(soma))