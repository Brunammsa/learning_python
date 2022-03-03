while True:
    primeiro_comando = int(input('\nDigite um valor aleatório >>> '))
    cubo = primeiro_comando * primeiro_comando
    quadrado = primeiro_comando ** 2
    cubica = round(primeiro_comando ** (1/3))
    if cubo == 0 or cubo < 0 or quadrado == 0 or quadrado < 0 or cubica == 0 or cubica < 0:
        print('\nSeu progroma parou porque alguma entrada deu um valor negativo ou igual a zero\n')
        break
    else:
        print('Cubo = {}, quadrado = {} e cubica = {}'.format(cubo, quadrado, cubica))
    