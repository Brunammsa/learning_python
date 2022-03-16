vetor = []
numeros_ordenados = []

opções = input("""
Menu:
0 para sair
1 para mostrar o vetor na ordem direta
2 para mostrar o vetor na ordem inversa

aperte 'enter' para continuar""")

for num in range(5):
    numero = int(input('Digite 5 números >>> '))
    vetor.append(numero)

while True:
    pergunta = int(input('Agora escolha uma das opções dadas no menu >>> '))
    if pergunta == 1:
        numeros_ordenados = sorted(vetor)
        print('A ordem dos números é:\n{}'.format(numeros_ordenados))
    elif pergunta == 2:
        vetor.reverse()
        print('A ordem inversa dos números é:\n{}'.format(vetor))
    elif pergunta == 0:
        break