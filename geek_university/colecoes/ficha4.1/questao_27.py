vetor = []
resposta = ''
numero = 2
quant_div = 0

while resposta != 'sair':
    n = int(input('Digite o tamanho da sequência >>> '))
    if n <= 1:
        print('número inválido')
    else:
        while numero <= n:
            for i in range(1, numero + 1):
                if numero % i == 0:
                    quant_div += 1
            if quant_div == 2:
                vetor.append(numero)
            numero += 1
            quant_div = 0
        print('dentre os números na sequência, {} são primos'.format(vetor))
        resposta = input('se deseja visualiza-los em posições, digite "sair" >>> ')

for i in enumerate(vetor):
    print(i)