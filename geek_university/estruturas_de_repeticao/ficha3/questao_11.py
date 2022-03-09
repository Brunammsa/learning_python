numero = 0
pergunta = int(input('Digite um número: '))

while numero <= pergunta:
    print(numero)
    numero += 1
if pergunta < 0:
    print('Número inválido, tente um natural positivo')
else:
    print('Fim')
