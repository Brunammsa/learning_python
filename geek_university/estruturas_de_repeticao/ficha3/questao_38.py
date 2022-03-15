# Terno Pitagórico
import math

resposta = ''

while resposta != 'sair':
    a = int(input('Digite o valor de "a" >>> '))
    b = int(input('Digite o valor de "b" >>> '))
    quadrado_de_a = a ** 2
    quadrado_de_b = b ** 2
    a_b = quadrado_de_a + quadrado_de_b
    raiz = math.sqrt(a_b)
    print('{}² + {}² = {} + {} = {} = {}²'.format(a, b, quadrado_de_a, quadrado_de_b, a_b, raiz))
    resposta = input('Se deseja continuar, aperte "enter", se não, digite "sair" >>> ')
