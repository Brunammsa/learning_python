valores = []

while True:
    pergunta_valores = int(input('Digite 6 valores >>> '))
    valores.append(pergunta_valores)
    if len(valores) == 6:
        break
print(valores)