resposta_finalizar = ' '


while resposta_finalizar != 'sair':
    km = int(input('Digite o valor pra km >>> '))
    ms = int(input('Digite o valor para m/s >>> '))
    km_para_ms = round(km / 3.6,2)
    ms_para_km = round(ms * 3.6,2)
    print('A conversão de km -> m/s é de {} e vice versa {}'.format(km_para_ms, ms_para_km))
    resposta_finalizar = input('\nSe deseja parar a conversão, digite "sair" para finalizar, se não, aperte o ENTER\n')
