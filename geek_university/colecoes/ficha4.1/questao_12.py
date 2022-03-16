valores = []
soma_valores = 0

for numeros in range(5):
    pergunta = float(input('Digite 5 números >>> '))
    valores.append(pergunta)
    soma_valores += pergunta
print(valores)
print('o maior valor digitado foi o {}'.format(max(valores)))
print('o menor valor digitado foi o {}'.format(min(valores)))
print('a média dos valores digitados foi de {}'.format(soma_valores/5))