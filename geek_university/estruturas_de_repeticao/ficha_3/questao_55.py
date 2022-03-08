numero_limite = int(input('Digite um número inteiro e positivo >>> '))

soma = 0
numero_inicial = 2 # Começa no 2 porquê 1 não é primo

if numero_limite <= 1:
    print('Tente novamente')
else:
    for i in range(numero_inicial, numero_limite+1):
        if numero_inicial % i == 0:
            print(numero_inicial)
            soma += numero_inicial
        numero_inicial += 1
    print('\nA soma dos termos primos é de {}'.format(soma))
    
# Não to sabendo deixar só os primos nessa questão