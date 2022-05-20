from questao_20 import fatorial

def super_fatorial(n):
    multi_super_fatorial = 1
    for i in range(n, 0, - 1):
        multi_super_fatorial = multi_super_fatorial * fatorial(i)
    return multi_super_fatorial

print(super_fatorial(4))
