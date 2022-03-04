print('''
~~~~~ Menu ~~~~

Digite a opção desejada:
- Adição (Opção 1)
- Subtração (Opção 2)
- Multiplicação (opção 3)
- Divisão (Opção 4)
- Sair (Opção 5)
''')

opcao_sair = ' '

while opcao_sair != 'Opção 5':
    opcao_desejada = input('Qual opção deseja selecionar? ')
    a = int(input('Digite o valor de "a" >>> '))
    b = int(input('Digite o valor de "b" >>> '))
    if opcao_desejada == 'Opção 1':
        print('{} + {} = {}'.format(a, b, a+b))
    elif opcao_desejada == 'Opção 2':
        print('{} - {} = {}'.format(a, b, a-b))
    elif opcao_desejada == 'Opção 3':
        print('{} * {} = {}'.format(a, b, a*b))
    elif opcao_desejada == 'Opção 4':
        print('{} / {} = {}'.format(a, b, a/b))
    opcao_sair = input('Deseja continuar? Caso não, escolha a Opção 5 >>> ')
