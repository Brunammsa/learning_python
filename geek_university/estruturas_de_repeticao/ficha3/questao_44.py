# Sequência de Fibonacci com repetição
numero = int(input('Digite a quantidade de termos para a sequência de Fibonacci >>> '))

t1 = 0
t2 = 1
contador = 3
print('{} {}'.format(t1, t2), end='')

while contador <= numero:
    t3 = t1 + t2
    print(' {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    contador += 1
    

# Não é exatamente o que a questão pede, mas a sequência ta feita