final_do_intervalo = int(input('Digite um valor para o final do intervalo >>> '))
soma_dos_quadrados = 0
soma_do_quadrado_da_soma = 0
valor = 1

while valor <= final_do_intervalo:
    soma_dos_quadrados += valor ** 2
    soma_do_quadrado_da_soma += valor
    valor += 1
print('A soma dos quadrados dos {} primeiros números naturais é {}'.format(final_do_intervalo, soma_dos_quadrados))
print('O quadrado da soma dos {} primeiros números naturais é de {}² = {}'.format(final_do_intervalo, soma_do_quadrado_da_soma, soma_do_quadrado_da_soma ** 2))
print('A diferença entre a soma dos quadrados dos {} primeiros números naturais e o quadrado da soma é de {} - {} = {}'.format(final_do_intervalo, soma_do_quadrado_da_soma ** 2, soma_dos_quadrados, soma_do_quadrado_da_soma ** 2-soma_dos_quadrados))