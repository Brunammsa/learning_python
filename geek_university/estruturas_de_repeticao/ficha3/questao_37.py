numero = ''
while numero != 'sair':
    numero = int(input('Digite um número entre 1000 e 9999 >>> '))
    if numero < 1000 or numero > 9999:
        print('Número inválido, digite entre 1000 e 9999')
    mais_baixa_ordem = numero // 100 % 100 # // quer dizer divisão inteira
    mais_alta_ordem = numero // 1 % 100
    if (mais_baixa_ordem + mais_alta_ordem) ** 2 == numero:
        print('Deu certo! ({} + {})² = {}'.format(mais_baixa_ordem, mais_alta_ordem, numero))
    else:
        print('Tente novamente')
        numero = input('Se deseja continuar tentando aperte "enter", se não, digite "sair" >>> ')