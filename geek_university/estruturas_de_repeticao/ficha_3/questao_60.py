print('''
~~~~~ OPÇÕES ~~~~~
a) A soma dos números digitados
b) A quantidade dos números digitados
c) A média dos números digitados
d) O maior número digitado
e) O menor número digitado
f) A média dos números pares
''')

opcao_sair = ' '
soma_valores = 0
contador = 0
termos_pares = 0

while opcao_sair != "0":
    valor_01 = int(input('Infome um valor >>> '))
    contador += 1
    valor_02 = int(input('Informe outro valor >>> '))
    contador += 1
    soma_valores = valor_01 + valor_02
    escolha_opcao = input('Escolha uma das opções acima >>> ')
    if escolha_opcao == 'a':
        print('{} + {} = {}'.format(valor_01, valor_02, valor_01+valor_02))
    elif escolha_opcao == 'b':
        print('você digitou {} valores'.format(contador)) # Não acho que fiz do jeito mais correto
    elif escolha_opcao == 'c':
        print('A média dos números digitados é de {}'.format(soma_valores/contador))
    elif escolha_opcao == 'd':
        if valor_01 > valor_02:
            print('{} é maior do que {}'.format(valor_01, valor_02))
        elif valor_02 > valor_01:
            print('{} é maior do que {}'.format(valor_02, valor_01))
    elif escolha_opcao == 'e':
        if valor_01 < valor_02:
            print('{} é menor do que {}'.format(valor_01, valor_02))
        elif valor_02 < valor_01:
            print('{} é menor do que {}'.format(valor_02, valor_01))
    elif escolha_opcao == 'f':
        for i in range(valor_01, valor_02, 2):
            termos_pares += i
        print('A média dos números pares é de {}'.format(termos_pares/contador))
    opcao_sair = input('Se deseja finalizar, digite 0, se não, aperte enter ')
