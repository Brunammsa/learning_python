# 1) Criar uma variavel maior_numero = 0 (ERRADO)
numeros_digitados = 3
maior_numero = 0

for _ in range(1, numeros_digitados + 1):
    numero_digitado = int(input("Digite um número:\n"))

    if (numero_digitado > maior_numero):
        maior_numero = numero_digitado

print("O maior número é: {}".format(maior_numero))

# A questão está errada pois se o usuário digitar -1, -2 e -3 o resultado vai ser 0

#####################################
# 2) Estratégia do -INF (Uma solução)
numeros_digitados = 3
maior_numero = float("-inf")

for _ in range(1, numeros_digitados + 1):
    numero_digitado = int(input("Digite um número:\n"))

    if (numero_digitado > maior_numero):
        maior_numero = numero_digitado

print("O maior número é: {}".format(maior_numero))
# A questão está correta

#################################
# 3) Guri's style (Outra solução)
numeros_digitados = 3
maior_numero = 0  # poderia ser qualquer valor aqui, a variável maior_numero vai ser sobrescrita no index == 1

for i in range(1, numeros_digitados + 1):
    numero_digitado = int(input("Digite um número:\n"))

    if (i == 1):
        maior_numero = numero_digitado

    if (numero_digitado > maior_numero):
        maior_numero = numero_digitado

print("O maior número é: {}".format(maior_numero))
# A questão está correta
