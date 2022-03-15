iteracao_mensal = 0
resposta = ''



while resposta != 'sair':
    salario_carlos = float(input('Qual o valor do salário de Carlos? >>> '))
    salario_joao = round(salario_carlos / 3,2)
    taxa_carlos = int(input('Informe a taxa de rendimento mensal de Carlos >>> '))
    taxa_joao = int(input('Informe a taxa de rendimento mensal de João >>> '))
    rendimento_carlos_ao_mes = salario_carlos * (taxa_carlos/100)
    rendimento_joao_ao_mes = salario_joao * (taxa_joao/100)
    aplicacao_carlos = salario_carlos + rendimento_carlos_ao_mes
    aplicacao_joao = salario_joao + rendimento_joao_ao_mes
    if rendimento_joao_ao_mes > rendimento_carlos_ao_mes:
        print('Para ultrapassar o valor pertencente a Carlos, João levou {} meses'.format(iteracao_mensal))
    elif rendimento_joao_ao_mes == rendimento_carlos_ao_mes:
        print('Para igualar os valores de Carlos, João levou {} meses'.format(iteracao_mensal))
    else:
        print('O rendimento de João ainda esta abaixo do esperado para se igualar ou ultrapassar o de Carlos')
        iteracao_mensal += 1
    resposta = input('Se deseja continuar tentando, aperte "enter", caso não, digite "sair" >>> ')

# Continuar o raciocínio depois