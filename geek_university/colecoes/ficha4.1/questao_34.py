vetor = []
numero = 0

while numero < 10:
    pergunta = int(input('Digite número >>> '))
    if pergunta in vetor:
        print('este número já existe, entre com outro')
    else:
        vetor.append(pergunta)
        numero += 1
print(vetor)
