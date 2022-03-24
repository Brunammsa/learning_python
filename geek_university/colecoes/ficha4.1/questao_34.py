vetor = []

for i in range(10):
    pergunta = int(input('Digite número >>> '))
    vetor.append(pergunta)
for numb in vetor:
    if pergunta == numb:
        print('este número já existe, entre com outro')
print(vetor)

#larguei, ver no outro dia