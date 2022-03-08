quantidade_linhas = int(input('Leia um número positivo inteiro >>> '))
iteracao_dos_termos = 1

if quantidade_linhas < 0:
    print('Número inválido, tente novamente')

for linhas in range(1, quantidade_linhas + 1):
    for termos in range(1, linhas +1):
        print(iteracao_dos_termos, end=' ')
        iteracao_dos_termos += 1
    print()
# Difícil p entender, precisa nomear bem as variáveis