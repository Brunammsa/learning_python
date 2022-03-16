from collections import Counter


valores_totais = []
valores_repetidos = []
repeticoes = []

for numb in range(10):
    numeros = int(input('Digite 10 números >>> '))
    valores_totais.append(numeros)

for numb in valores_totais:
    if valores_totais.count(numb) > 1:
        valores_repetidos.append(numb)

repeticoes = Counter(valores_repetidos)
print(repeticoes)


