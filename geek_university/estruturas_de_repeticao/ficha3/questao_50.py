altura_chico = 1.50
altura_ze = 1.10

iteracao_ano = 0

while altura_ze < altura_chico:
    altura_chico += 0.02
    altura_ze += 0.03
    iteracao_ano +=1
    if altura_ze > altura_chico:
        print('Foram necessários {} anos para que Zé seja maior do que Chico'.format(iteracao_ano))
